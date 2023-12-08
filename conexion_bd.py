# conexion_bd.py
import psycopg2

def conectar_bd():
    print("Conexión a la base de datos establecida")

    # Configura estos valores con la información de tu base de datos PostgreSQL
    db_config = {
        'HOST': 'localhost',  # Puedes cambiarlo según la ubicación de tu base de datos
        'NAME': 'Eventos',
        'USER': 'postgres',
        'PASSWORD': 'awayouname11',
    }

    # Simular conexión a una base de datos PostgreSQL
    connection = psycopg2.connect(**db_config)
    return connection