import mysql.connector
from funcion import *

def ejecutar_consulta(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

base = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_project"
)

cursor = base.cursor()
insertarDatos(base, cursor)

alter_query = "ALTER TABLE tu_tabla ADD columna_nueva INT"
cursor.execute(alter_query)
base.commit()

delete_query = "DELETE FROM tu_tabla WHERE condicion"
cursor.execute(delete_query)
base.commit()

select_query = "SELECT * FROM tu_tabla WHERE columna = 'valor'"
ejecutar_consulta(cursor, select_query)
cursor.close()
base.close()
