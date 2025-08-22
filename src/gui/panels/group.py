import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

from src.services.group_service import GroupService
from src.gui.panels.panel import Panel

class CreateGroupFrame(Panel):
    def __init__(self, parent, *args, **kwargs):
        # Panel already sets fg_color and pack_propagate
        super().__init__(parent, *args, **kwargs)

        # --- Estilo común para botones ---
        self.accent_color = "#E7880D"
        self.entry_font = ("Facebook Sans", 16)
        self.btn_style = {
            "fg_color": self.accent_color,
            "hover_color": "#D97C0C",
            "font": ("Facebook Sans", 18),
            "height": 50
        }

        # --- Icons ---
        save_icon = CTkImage(Image.open("assets/icons/check_light.png"), size=(24, 24))
        cancel_icon = CTkImage(Image.open("assets/icons/close_light.png"), size=(24, 24))
        group_icon = CTkImage(Image.open("assets/icons/group_logo_light.png"), size=(24, 24))

        # Variable de selección (1 = usar existente, 2 = crear nueva)
        self.category_mode = ctk.IntVar(value=1)

        # --- Título ---
        self.title_label = ctk.CTkLabel(
            self, text="Crear / Editar Grupo", 
            font=("Facebook Sans", 26),
            text_color="white"
        )
        self.title_label.pack(pady=(15, 20))

        # --- Contenedor de dos columnas ---
        self.form_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.form_frame.pack(fill="both", expand=True, padx=20)
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=1)

        # --- Campo: Nombre ---
        self.name_entry = ctk.CTkEntry(
            self.form_frame, placeholder_text="Nombre del grupo", height=45,
            font=self.entry_font
        )
        self.name_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # --- Campo: URL ---
        self.url_entry = ctk.CTkEntry(
            self.form_frame, placeholder_text="URL del grupo (opcional)", height=45,
            font=self.entry_font
        )
        self.url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # --- Campo: Descripción (ocupa 2 columnas) ---
        self.desc_text = ctk.CTkTextbox(self.form_frame, height=140, font=self.entry_font)
        self.desc_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.desc_text.insert("0.0", "Descripción del grupo...")

        # --- Categoría ---
        self.category_label = ctk.CTkLabel(
            self.form_frame, text="Categoría", 
            font=("Facebook Sans", 22),
            text_color="white"
        )
        self.category_label.grid(row=2, column=0, columnspan=2, pady=(15,5))

        # RadioButton estilo acento
        self.radio_existing = ctk.CTkRadioButton(
            self.form_frame, text="Usar categoría existente", 
            variable=self.category_mode, value=1,
            fg_color=self.accent_color, hover_color="#D97C0C",
            command=self.toggle_category_mode, text_color="white",
            font=self.entry_font
        )
        self.radio_existing.grid(row=3, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        # Dropdown para categorías existentes (ocupa columna izquierda)
        self.category_menu = ctk.CTkOptionMenu(
            self.form_frame, values=["Categoría 1", "Categoría 2"],
            fg_color=self.accent_color, button_color=self.accent_color, 
            button_hover_color="#D97C0C", dropdown_fg_color="#2C2C2C", 
            text_color="white", font=self.entry_font, dropdown_font=self.entry_font
        )
        self.category_menu.grid(row=4, column=0, padx=40, pady=5, sticky="ew")

        # RadioButton para crear nueva categoría
        self.radio_new = ctk.CTkRadioButton(
            self.form_frame, text="Crear nueva categoría", 
            variable=self.category_mode, value=2,
            fg_color=self.accent_color, hover_color="#D97C0C",
            command=self.toggle_category_mode, text_color="white",
            font=self.entry_font
        )
        self.radio_new.grid(row=5, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        # Campo nueva categoría (columna izquierda)
        self.new_category_entry = ctk.CTkEntry(
            self.form_frame, placeholder_text="Nombre nueva categoría", height=45,
            font=self.entry_font
        )
        self.new_category_entry.grid(row=6, column=0, padx=40, pady=5, sticky="ew")

        # --- Contenedor para botones Guardar y Cancelar ---
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=(10, 20))

        self.save_btn = ctk.CTkButton(
            self.buttons_frame, text="Save", **self.btn_style, width=180, image = save_icon
        )
        self.save_btn.grid(row=0, column=0, padx=10)

        self.cancel_btn = ctk.CTkButton(
            self.buttons_frame, text="Cancel", **self.btn_style, width=180, image = cancel_icon
        )
        self.cancel_btn.grid(row=0, column=1, padx=10)

        self.toggle_category_mode()

    def toggle_category_mode(self):
        """Habilita/deshabilita campos según el modo de categoría."""
        if self.category_mode.get() == 1:
            self.category_menu.configure(state="normal")
            self.new_category_entry.configure(state="disabled")
        else:
            self.category_menu.configure(state="disabled")
            self.new_category_entry.configure(state="normal")
            self.new_category_entry.configure(state="normal")
