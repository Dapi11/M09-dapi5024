import mysql.connector

def GetMail():
    mycursos = mydb.cursor()
    buscarMail = str(input("Dime un nombre y te digo el mail: "))
    mycursos.execute("SELECT Correo FROM alumnos WHERE Nombre = %s",(buscarMail,))
    myresult = mycursos.fetchall()
    if myresult:
        for x in myresult:
            print(x)
    else:
        print("No he encontrado ese nombre, vuelve a intentarlo.")

def AddUser():
    mycursor = mydb.cursor()
    nombre=str(input("dime tu nombre: "))
    correo=str(input("dime tu correo: "))
    mycursor.execute("INSERT INTO alumnos (Nombre, Correo) VALUES (%s, %s)", (nombre,correo))
    mydb.commit()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="aplicaciones_web"
)

while True:
    print("\n----------MENU---------- \n1. Obtener correo electrónico por nombre\n2. Agregar nuevo usuario\n3. Salir\n------------------------")  
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        GetMail()
    elif opcion == "2":
        AddUser()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
