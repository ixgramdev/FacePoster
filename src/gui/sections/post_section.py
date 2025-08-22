import customtkinter as ctk

class PostSection(ctk.CTkFrame):
    def __init__(self, parent, width=600, height=400, *args, **kwargs):
        # Definir color negro para el frame
        kwargs["fg_color"] = "#000000"  # Color negro
        super().__init__(parent, width=width, height=height, *args, **kwargs)
        
        # Expandir para ocupar todo el contenedor padre
        self.pack_propagate(False)

        # Título de la sección
        self.title_label = ctk.CTkLabel(self, text="Publicaciones", font=("Facebook Sans", 24), text_color="white")
        self.title_label.pack(pady=20)
        
        # Frame para la lista de grupos
        self.list_frame = ctk.CTkFrame(self, fg_color="#111111")  # Fondo ligeramente distinto para diferenciar
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Ejemplo de grupo
        self.example_group = ctk.CTkLabel(self.list_frame, text="Publicación Ejemplo", font=("Facebook Sans", 18), text_color="white")
        self.example_group.pack(pady=5)
        
        # Botón de acción
        self.add_group_btn = ctk.CTkButton(self, text="Crear Publicación", command=self.add_group)
        self.add_group_btn.pack(pady=10)

    def add_group(self):
        print("Agregar grupo ejecutado")
