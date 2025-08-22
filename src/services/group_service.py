import sqlite3
from typing import List, Optional, Dict
from src.utils.init_db import DB_PATH  # <-- importamos la ruta correcta

class GroupService:

    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    # ------------------ CREATE ------------------
    def create_group(self, name: str, description: str, category_id: int, image_path: Optional[str] = None, url: Optional[str] = None) -> int:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO grupos (nombre, descripcion, imagen, categoria_id, url)
            VALUES (?, ?, ?, ?, ?)
        """, (name, description, image_path, category_id, url))
        conn.commit()
        group_id = cursor.lastrowid
        conn.close()
        return group_id

    # ------------------ READ ------------------
    def get_group(self, group_id: int) -> Optional[Dict]:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grupos WHERE id = ?", (group_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {
                "id": row[0],
                "nombre": row[1],
                "descripcion": row[2],
                "imagen": row[3],
                "categoria_id": row[4],
                "url": row[5]
            }
        return None

    def get_all_groups(self) -> List[Dict]:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grupos")
        rows = cursor.fetchall()
        conn.close()
        return [
            {
                "id": row[0],
                "nombre": row[1],
                "descripcion": row[2],
                "imagen": row[3],
                "categoria_id": row[4],
                "url": row[5]
            }
            for row in rows
        ]

    # ------------------ UPDATE ------------------
    def edit_group(self, group_id: int, new_name: Optional[str] = None,
                   new_description: Optional[str] = None,
                   new_category_id: Optional[int] = None,
                   new_image_path: Optional[str] = None,
                   new_url: Optional[str] = None) -> bool:
        conn = self._connect()
        cursor = conn.cursor()
        updates = []
        params = []

        if new_name is not None:
            updates.append("nombre = ?")
            params.append(new_name)
        if new_description is not None:
            updates.append("descripcion = ?")
            params.append(new_description)
        if new_category_id is not None:
            updates.append("categoria_id = ?")
            params.append(new_category_id)
        if new_image_path is not None:
            updates.append("imagen = ?")
            params.append(new_image_path)
        if new_url is not None:
            updates.append("url = ?")
            params.append(new_url)

        if not updates:
            return False  # Nada que actualizar

        params.append(group_id)
        query = f"UPDATE grupos SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, tuple(params))
        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()
        return updated

    # ------------------ DELETE ------------------
    def delete_group(self, group_id: int) -> bool:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM grupos WHERE id = ?", (group_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
