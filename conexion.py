import mysql
import mysql.connector
from mysql.connector import errorcode


def get_db_connection():
       
# Datos de conexión a la base de datos MySQL
    config = {
                'user': 'root',
                'password': 'Admin23',
                'host': 'localhost',
                'database': 'parking_now',
                'raise_on_warnings': True
            }

    
    try:
        cnx = mysql.connector.connect(**config)
        print("Conexión a la base de datos establecida correctamente.")  # Mensaje de éxito
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Usuario o contraseña incorrectos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: La base de datos no existe.")
        else:
            print(f"Error al conectar a la base de datos: {err}")
        return None

