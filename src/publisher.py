import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .config import DELAY_MIN, DELAY_MAX, SELENIUM_TIMEOUT
from .utils import setup_logger
import logging

def publicar_en_grupos(csv_path):
    setup_logger()
    from .utils import leer_productos
    productos = leer_productos(csv_path)

    if not productos:
        logging.error("No se encontraron productos en el CSV.")
        print("No hay productos para publicar.")
        return

    # Inicializar Selenium
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Abrir Facebook y esperar login manual
    driver.get("https://www.facebook.com/")
    input("Inicia sesión manualmente en Facebook y presiona ENTER aquí...")

    for p in productos:
        grupo = p["grupo_url"]
        mensaje = p["mensaje"]
        imagenes = p["imagenes"]

        try:
            driver.get(grupo)
            WebDriverWait(driver, SELENIUM_TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
            )

            # Escribir el mensaje
            caja = driver.find_element(By.XPATH, "//div[@role='textbox']")
            caja.click()
            time.sleep(2)
            caja.send_keys(mensaje)

            # Subir imágenes si existen
            if imagenes:
                try:
                    input_file = driver.find_element(By.XPATH, "//input[@type='file']")
                    input_file.send_keys("\n".join(imagenes))
                    time.sleep(5)  # dar tiempo a subir imágenes
                except Exception as e:
                    logging.warning(f"No se pudo subir imágenes: {e}")

            # Botón publicar (este selector puede variar según idioma/interfaz)
            try:
                boton = driver.find_element(By.XPATH, "//div[@aria-label='Publicar' or @aria-label='Post']")
                boton.click()
                logging.info(f"Publicado en {grupo}: {mensaje[:50]}...")
                print(f"Publicado en {grupo}")
            except Exception as e:
                logging.error(f"No se encontró el botón de publicar: {e}")
                print(f"Error al publicar en {grupo}")

            # Pausa aleatoria
            time.sleep(random.randint(DELAY_MIN, DELAY_MAX))

        except Exception as e:
            logging.error(f"Error con el grupo {grupo}: {e}")
            print(f"Error con el grupo {grupo}")

    driver.quit()
