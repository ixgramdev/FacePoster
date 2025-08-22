# src/gui/components/group_card.py
import customtkinter as ctk
from PIL import Image, ImageTk
import os

class GroupCard(ctk.CTkFrame):
    def __init__(self, parent, nombre, descripcion, categoria, imagen_path=None, width=400, height=120, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs)
        self.pack_propagate(False)  # Evitar que el frame cambie de tamaño automáticamente

        # Imagen del grupo
        if imagen_path and os.path.exists(imagen_path):
            img = Image.open(imagen_path).resize((80, 80))
        else:
            # Imagen por defecto si no hay
            img = Image.new("RGB", (80, 80), color="#CCCCCC")
        self.photo = ImageTk.PhotoImage(img)

        self.img_label = ctk.CTkLabel(self, image=self.photo, text="")
        self.img_label.pack(side="left", padx=10, pady=10)

        # Frame de texto (nombre, descripción, categoría)
        text_frame = ctk.CTkFrame(self, fg_color="transparent")
        text_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.lbl_nombre = ctk.CTkLabel(text_frame, text=nombre, font=ctk.CTkFont(size=16, weight="bold"))
        self.lbl_nombre.pack(anchor="w")

        self.lbl_descripcion = ctk.CTkLabel(text_frame, text=descripcion, font=ctk.CTkFont(size=12), wraplength=250, justify="left")
        self.lbl_descripcion.pack(anchor="w", pady=2)

        self.lbl_categoria = ctk.CTkLabel(text_frame, text=f"Categoría: {categoria}", font=ctk.CTkFont(size=11), text_color="#E7880D")
        self.lbl_categoria.pack(anchor="w", pady=2)



    


