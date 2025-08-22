import customtkinter as ctk

class Dashboard(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill="both", expand=True)
        self._crear_widgets()

    def _crear_widgets(self):
        self.lbl_titulo = ctk.CTkLabel(self, text="Dashboard", font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_titulo.pack(pady=20)

        self.txt_info = ctk.CTkTextbox(self, width=600, height=400)
        self.txt_info.pack(pady=10)

    def agregar_info(self, mensaje):
        self.txt_info.insert(ctk.END, mensaje + "\n")
        self.txt_info.see(ctk.END)