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

def leer_productos(path_csv):
    productos = []
    with open(path_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            grupo_url = row.get("grupo_url", "").strip()
            mensaje = row.get("mensaje", "").strip()
            imagenes = [img.strip() for img in row.get("imagenes", "").split(",") if img.strip()]
            if grupo_url and mensaje:
                productos.append({
                    "grupo_url": grupo_url,
                    "mensaje": mensaje,
                    "imagenes": imagenes
                })
    return productos
