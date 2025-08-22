import os
from PIL import Image
from customtkinter import CTkImage
import customtkinter as ctk

from src.utils.utils import load_font


class Header(ctk.CTkFrame):
    def __init__(self, parent, logo_path="assets/logo.png", app_name="facePoster", *args, **kwargs):
        super().__init__(parent, fg_color="transparent", *args, **kwargs)
        
        # Crear contenedor horizontal
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(pady=20)

        # Añadir logo y nombre
        self._set_logo(header_frame, logo_path)
        self._set_name_app(header_frame, app_name)

    def _set_logo(self, parent, path):
        if os.path.exists(path):
            pil_image = Image.open(path)
            logo_image = CTkImage(light_image=pil_image, dark_image=pil_image, size=(50, 50))
            logo_label = ctk.CTkLabel(parent, image=logo_image, text="")
            logo_label.image = logo_image  # evita que el recolector de basura la borre
            logo_label.pack(side="left", padx=10)
        else:
            print(f"Logo file not found: {path}")

    def _set_name_app(self, parent, name):
        name_brand = ctk.CTkLabel(parent, text=name, text_color="#FFFFFF", font= ("FaceBook Sans", 30))
        name_brand.pack(side="left")
