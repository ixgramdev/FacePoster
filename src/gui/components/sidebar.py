import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

class SideBar(ctk.CTkFrame):
    def __init__(self, parent, show_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.show_frame_callback = show_frame_callback
        self.configure(width=200, corner_radius=0)

        # Estilo común para los botones
        btn_style = {
            "fg_color": "#E7880D",
            "hover_color": "#D97C0C",
            "font": ("Facebook Sans", 16),
            "height": 50
        }

        # Cargar iconos
        dashboard_icon = CTkImage(Image.open("assets/icons/dashboard_light.png"), size=(24, 24))
        groups_icon = CTkImage(Image.open("assets/icons/groups_light.png"), size=(24, 24))
        publications_icon = CTkImage(Image.open("assets/icons/post_light.png"), size=(24, 24))

        # Botón Dashboard
        self.btn_dashboard = ctk.CTkButton(
            self, text="Dashboard",
            command=lambda: self.show_frame_callback("dashboard"),
            image=dashboard_icon,
            compound="left",
            **btn_style
        )
        self.btn_dashboard.pack(pady=5, padx=10, fill="x")

        # Botón Publicaciones
        self.btn_groups = ctk.CTkButton(
            self, text="Publications",
            command=lambda: self.show_frame_callback("publications"),
            image=publications_icon,
            compound="left",
            **btn_style
        )
        self.btn_groups.pack(pady=5, padx=10, fill="x")

        # Botón Groups
        self.btn_groups = ctk.CTkButton(
            self, text="Groups",
            command=lambda: self.show_frame_callback("groups"),
            image=groups_icon,
            compound="left",
            **btn_style
        )
        self.btn_groups.pack(pady=5, padx=10, fill="x")


