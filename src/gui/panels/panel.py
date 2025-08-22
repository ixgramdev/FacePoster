import customtkinter as ctk

class Panel(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        # Configuración básica de fondo
        kwargs["fg_color"] = "#2C2C2C"
        super().__init__(parent, *args, **kwargs)
        self.pack_propagate(False)

    # ---------------- Métodos de visibilidad ----------------
    def show_(self):
        """Muestra el panel."""
        self.pack(fill="both", expand=True)

    def hide(self):
        """Oculta el panel."""
        self.pack_forget()

    # ---------------- Método de carga de datos ----------------
    def load_data(self):
        """
        Método genérico para cargar datos en el panel.
        Debe ser sobrescrito por las subclases.
        """
        pass
