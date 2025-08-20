import customtkinter as ctk
import threading
import os
from tkinter import filedialog, END
from .utils import leer_productos
from .publisher import publicar_en_grupos

class FacePosterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FacePoster")
        self.geometry("700x500")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Variables
        self.csv_path = ctk.StringVar(value="data/productos.csv")
        self.productos = []

        # --- Interfaz ---
        self._crear_widgets()

    def _crear_widgets(self):
        # Frame superior
        frame_top = ctk.CTkFrame(self)
        frame_top.pack(pady=10, padx=10, fill="x")

        # Botón para cargar CSV
        self.btn_cargar = ctk.CTkButton(frame_top, text="Cargar CSV", command=self.cargar_csv)
        self.btn_cargar.pack(side="left", padx=5)

        # Etiqueta de archivo actual
        self.lbl_csv = ctk.CTkLabel(frame_top, textvariable=self.csv_path)
        self.lbl_csv.pack(side="left", padx=5)

        # Frame central (vista previa productos)
        frame_mid = ctk.CTkFrame(self)
        frame_mid.pack(pady=10, padx=10, fill="both", expand=True)

        self.txt_productos = ctk.CTkTextbox(frame_mid, wrap="word")
        self.txt_productos.pack(fill="both", expand=True, padx=5, pady=5)

        # Frame inferior (botón publicar)
        frame_bottom = ctk.CTkFrame(self)
        frame_bottom.pack(pady=10, padx=10, fill="x")

        self.btn_publicar = ctk.CTkButton(frame_bottom, text="Publicar en grupos", command=self.iniciar_publicacion)
        self.btn_publicar.pack(side="left", padx=5)

        self.txt_log = ctk.CTkTextbox(frame_bottom, wrap="word", height=100)
        self.txt_log.pack(side="left", fill="x", expand=True, padx=5)

    def cargar_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.csv_path.set(file_path)
            self.productos = leer_productos(file_path)
            self._mostrar_productos()

    def _mostrar_productos(self):
        self.txt_productos.delete("1.0", END)
        if not self.productos:
            self.txt_productos.insert(END, "No hay productos cargados.\n")
        else:
            for i, p in enumerate(self.productos, start=1):
                self.txt_productos.insert(END, f"{i}. Grupo: {p['grupo_url']}\n")
                self.txt_productos.insert(END, f"   Mensaje: {p['mensaje'][:50]}...\n")
                self.txt_productos.insert(END, f"   Imágenes: {', '.join(p['imagenes']) or 'Sin imágenes'}\n\n")

    def iniciar_publicacion(self):
        # Usamos threading para no congelar la GUI
        t = threading.Thread(target=self._publicar_thread)
        t.start()

    def _publicar_thread(self):
        self.txt_log.insert(END, "Iniciando publicación...\n")
        publicar_en_grupos(self.csv_path.get())
        self.txt_log.insert(END, "Publicación terminada.\n")

def run_gui():
    app = FacePosterApp()
    app.mainloop()
