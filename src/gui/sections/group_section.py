import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

from src.gui.panels.group import CreateGroupFrame

class GroupSection(ctk.CTkFrame):
    def __init__(self, parent, width=600, height=400, *args, **kwargs):
        kwargs["fg_color"] = "#212121"
        super().__init__(parent, width=width, height=height, *args, **kwargs)
        self.pack_propagate(False)

        # --- Estilos Botones ---
        self.btn_style = {
            "fg_color": "#E7880D",
            "hover_color": "#D97C0C",
            "font": ("Facebook Sans", 16),
            "height": 50
        }

        # --- Iconos ---
        self.add_group_icon = CTkImage(Image.open("assets/icons/add_group_light.png"), size=(24, 24))
        
        # --- Título ---
        self.title_label = ctk.CTkLabel(
            self, text="Grupos", 
            font=("Facebook Sans", 24), 
            text_color="white"
        )
        self.title_label.pack(pady=20)

        # --- Frame con scroll para la lista ---
        self.list_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=(0, 50))
        self.list_frame.grid_columnconfigure(0, weight=1)

        # --- Botón flotante ---
        self.add_group_btn = ctk.CTkButton(
            self, text="Add Group",
            command=self.show_create_group_frame,
            image=self.add_group_icon,
            compound="left",
            **self.btn_style
        )
        self.add_group_btn.place(relx=1.0, rely=1.0, x=-50, y=-20, anchor="se")

        # --- Overlay para crear grupo (oculto al inicio) ---
        self.create_group_frame = CreateGroupFrame(self)
        self.create_group_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.create_group_frame.lower()  # lo manda al fondo para que no se vea al inicio

    def show_create_group_frame(self):
        """Muestra el frame para crear grupo sobre todos los widgets."""
        self.create_group_frame.lift()

    def hide_create_group_frame(self):
        """Oculta el frame para crear grupo enviándolo al fondo."""
        self.create_group_frame.lower()

    def load_groups(self, groups):
        """Recibe una lista de grupos y los muestra en list_frame."""
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        if not groups:
            empty_label = ctk.CTkLabel(
                self.list_frame, 
                text="No hay grupos disponibles", 
                font=("Facebook Sans", 16), 
                text_color="gray"
            )
            empty_label.grid(row=0, column=0, pady=5, sticky="w")
        else:
            for i, group in enumerate(groups):
                name = group["nombre"] if isinstance(group, dict) else group[1]
                label = ctk.CTkLabel(
                    self.list_frame, 
                    text=name, 
                    font=("Facebook Sans", 18), 
                    text_color="white"
                )
                label.grid(row=i, column=0, pady=5, sticky="w")
