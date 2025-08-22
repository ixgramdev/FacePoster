import csv
import logging
import os



# --- Configurar logger ---
def setup_logger():
    log_path = os.path.join("logs", "run.log")
    logging.basicConfig(
        filename=log_path,
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def leer_productos(csv_path):
    pass

def install_all_fonts():
    import shutil
    import sys
    """
    Instala todas las fuentes .ttf que estén en facePoster/assets/fonts
    según el sistema operativo (Windows y Linux).
    Se ejecuta solo la primera vez usando un archivo de control.
    """

    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # main.py
    print("Ruta en la que estamos yendo: " + str(project_root))
    fonts_dir = os.path.join(project_root, "assets/fonts")  # assets/fonts
    flag_file = os.path.join(project_root, ".fonts_installed")  # archivo de control


    if os.path.exists(flag_file):
        print("Fuentes ya instaladas, no se ejecuta la instalación.")
        return

    if not os.path.exists(fonts_dir):
        print(f"Directorio de fuentes no encontrado: {fonts_dir}")
        return

    system = sys.platform

    ttf_files = [f for f in os.listdir(fonts_dir) if f.lower().endswith(".ttf")]
    if not ttf_files:
        print("No se encontraron archivos .ttf en el directorio de fuentes.")
        return

    for ttf in ttf_files:
        ttf_path = os.path.join(fonts_dir, ttf)
        try:
            if system.startswith("win"):
                dest_dir = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts")
                destino = os.path.join(dest_dir, ttf)
                shutil.copy(ttf_path, destino)
                print(f"[Windows] Fuente instalada: {destino}")

            elif system.startswith("linux"):
                home_fonts = os.path.expanduser("~/.fonts")
                os.makedirs(home_fonts, exist_ok=True)
                destino = os.path.join(home_fonts, ttf)
                shutil.copy(ttf_path, destino)
                os.system("fc-cache -f -v")
                print(f"[Linux] Fuente instalada: {destino}")

            else:
                print(f"Sistema {system} no soportado para instalación automática de fuentes.")

        except Exception as e:
            print(f"No se pudo instalar {ttf}: {e}")

    try:
        with open(flag_file, "w") as f:
            f.write("ok")
        print("Instalación de fuentes completada.")
    except Exception as e:
        print(f"No se pudo crear archivo de control: {e}")


def load_font(root, ttf_filename, font_name=None, default_size=12):
    import tkinter as tk
    """
    Registra un archivo TTF ubicado en 'assets/fonts/' desde la raíz del proyecto
    y devuelve el nombre de la fuente para usarla en widgets.
    """
    if font_name is None:
        font_name = os.path.splitext(ttf_filename)[0]

    # Calcular la raíz del proyecto (un nivel arriba de 'src')
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    font_path = os.path.join(project_root, "assets/fonts", ttf_filename)

    if os.path.exists(font_path):
        try:
            root.tk.call("font", "create", font_name, "-family", font_name, "-size", default_size)
            root.tk.call("font", "configure", font_name, "-family", font_name, "-size", default_size)
            return font_name
        except tk.TclError:
            print(f"No se pudo registrar la fuente {ttf_filename}, usando fuente por defecto")
    else:
        print(f"Archivo {font_path} no encontrado, usando fuente por defecto")

    return None


