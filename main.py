from logica_negocio import GestorTareas
from modulo_b import ArchivoB
from modulo_c import ArchivoC

def mostrar_menu():
    print("\n=== Menú ===")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Actualizar tarea")
    print("4. Eliminar tarea")
    print("5. Procesar tareas desde Archivo B")
    print("6. Agregar tarea desde Archivo C")
    print("0. Salir")

def ejecutar_menu(opcion, gestor_tareas, archivo_b, archivo_c):
    if opcion == 1:
        tareas = gestor_tareas.obtener_tareas()
        print("\nTareas:")
        for tarea in tareas:
            print(tarea)
    elif opcion == 2:
        descripcion = input("Ingrese la descripción de la nueva tarea: ")
        gestor_tareas.agregar_tarea(descripcion)
        print("Tarea agregada con éxito.")
    elif opcion == 3:
        tarea_id = int(input("Ingrese el ID de la tarea a actualizar: "))
        tarea = gestor_tareas.obtener_tarea_por_id(tarea_id)
        if tarea:
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            completada = input("¿La tarea está completada? (True/False): ").capitalize() == "True"
            gestor_tareas.actualizar_tarea(tarea_id, nueva_descripcion, completada)
            print("Tarea actualizada con éxito.")
        else:
            print(f"No se encontró la tarea con ID {tarea_id}.")
    elif opcion == 4:
        tarea_id = int(input("Ingrese el ID de la tarea a eliminar: "))
        gestor_tareas.eliminar_tarea(tarea_id)
        print("Tarea eliminada con éxito.")
    elif opcion == 5:
        archivo_b.procesar_tareas()
    elif opcion == 6:
        descripcion_c = input("Ingrese la descripción de la tarea desde Archivo C: ")
        archivo_c.agregar_tarea_desde_archivo_c(descripcion_c)
        print("Tarea agregada desde Archivo C con éxito.")
    elif opcion == 0:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida del menú.")

if __name__ == "__main__":
    # Reemplaza los siguientes valores con los de tu base de datos
    conexion_str = "dbname=Tareas user=postgres password=awayouname11 host=127.0.0.1 port=5432"
    
    gestor_tareas = GestorTareas(conexion_str)
    archivo_b = ArchivoB(gestor_tareas)
    archivo_c = ArchivoC(gestor_tareas)

    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción (0-6): "))
        ejecutar_menu(opcion, gestor_tareas, archivo_b, archivo_c)


from logica_negocio import GestorTareas
from modulo_b import ArchivoB
from modulo_c import ArchivoC

