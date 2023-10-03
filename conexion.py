import mysql.connector

#Conectar con la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mibasededatos"
)

#Crear un objeto cursor para realizar consultas SQL
mycursor = mydb.cursor()

#Ejecutar una consulta SQL para ver programa
mycursor.execute("SELECT * FROM tareas")
resultados = mycursor.fetchall()

for fila in resultados:
    print(fila)

#Cerrar el cursor y la conexion a la base de datos
mycursor.close()
mydb.close()
