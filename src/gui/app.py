import customtkinter as ctk

# Components
from .components.header import Header  
from src.utils.utils import install_all_fonts
from src.gui.sections.dashboard import Dashboard
from src.gui.sections.group_section import GroupSection
from .components.sidebar import SideBar
from src.gui.sections.post_section import PostSection

class FacePosterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FacePoster")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Contenedor Sidebar + Header
        self.sidebar_container = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_container.pack(side="left", fill="y")

        # Header sobre el sidebar
        header = Header(self.sidebar_container, logo_path="assets/logo.png", app_name="facePoster")
        header.pack(side="top", fill="x", padx=5, pady=1)

        # Sidebar debajo del header, ocupa todo el contenedor
        self.sidebar_frame = SideBar(self.sidebar_container, show_frame_callback=self.show_frame)
        self.sidebar_frame.pack(side="top", fill="both", expand=True)

        # Área de contenido (el resto del espacio)
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Frames
        self.frames = {}
        self.frames["dashboard"] = Dashboard(self)
        self.frames["groups"] = GroupSection(self)
        self.frames["publications"] = PostSection(self)

        # Mostrar frame por defecto
        self.show_frame("dashboard")

    def show_frame(self, name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[name].pack(in_=self.content_frame, fill="both", expand=True)


def run_gui():
    app = FacePosterApp()
    install_all_fonts()
    app.mainloop()
