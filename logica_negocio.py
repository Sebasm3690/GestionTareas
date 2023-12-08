import psycopg2

class GestorTareas:
    def __init__(self, conexion_str):
        self.conn = psycopg2.connect(conexion_str)
        self.crear_tabla()

    def crear_tabla(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tareas (
                    id SERIAL PRIMARY KEY,
                    descripcion TEXT,
                    completada BOOLEAN
                )
            """)
        self.conn.commit()

    def agregar_tarea(self, descripcion, completada=False):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO tareas (descripcion, completada) VALUES (%s, %s)
            """, (descripcion, completada))
        self.conn.commit()

    def obtener_tareas(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tareas")
            return cursor.fetchall()

    def obtener_tarea_por_id(self, tarea_id):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tareas WHERE id = %s", (tarea_id,))
            return cursor.fetchone()

    def actualizar_tarea(self, tarea_id, descripcion, completada):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                UPDATE tareas SET descripcion = %s, completada = %s WHERE id = %s
            """, (descripcion, completada, tarea_id))
        self.conn.commit()

    def eliminar_tarea(self, tarea_id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM tareas WHERE id = %s", (tarea_id,))
        self.conn.commit()
