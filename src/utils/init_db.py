# src/utils/init_db.py
import sqlite3
import os

DB_FOLDER = "data"
DB_PATH = os.path.join(DB_FOLDER, "database.db")

def crear_db():
    # Crear carpeta si no existe
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    # Conectar (esto crea el archivo si no existe)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabla de categorías
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL
    )
    """)

    # Tabla de grupos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grupos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        imagen TEXT,
        categoria_id INTEGER,
        url TEXT,
        FOREIGN KEY(categoria_id) REFERENCES categorias(id)
    )
    """)

    # Tabla de publicaciones (opcional)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publicaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        categoria_id INTEGER,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(categoria_id) REFERENCES categorias(id)
    )
    """)

    conn.commit()
    conn.close()
    print(f"Base de datos creada en {DB_PATH}")

if __name__ == "__main__":
    crear_db()