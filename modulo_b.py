class ArchivoB:
    def __init__(self, gestor_tareas):
        self.gestor_tareas = gestor_tareas

    def procesar_tareas(self):
        # Aquí puedes realizar operaciones relacionadas con la lógica de tareas
        tareas = self.gestor_tareas.obtener_tareas()
        print("Tareas en Archivo B:")
        for tarea in tareas:
            print(tarea)
