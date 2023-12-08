class ArchivoC:
    def __init__(self, gestor_tareas):
        self.gestor_tareas = gestor_tareas

    def agregar_tarea_desde_archivo_c(self, descripcion):
        # Aquí puedes realizar operaciones relacionadas con la lógica de tareas
        self.gestor_tareas.agregar_tarea(descripcion, completada=False)