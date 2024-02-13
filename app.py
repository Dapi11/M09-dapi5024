from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="aplicaciones_web"
)

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      user = request.form['name']
      mycursos = mydb.cursor()
      mycursos.execute("SELECT Correo FROM alumnos WHERE Nombre = %s",(user,))
      myresult = mycursos.fetchall()
      if myresult:
         for x in myresult:
            mail=x
            return render_template('resultado.html',mail=mail,user=user)
      else:
         return ("NO ENCONTRADO")
   else:
      return render_template('formulario_getmail.html')

@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      user = request.form['name']
      mail = request.form['mail']
      mycursos = mydb.cursor()
      mycursos.execute("SELECT Correo FROM alumnos WHERE Nombre = %s",(user,))
      myresult = mycursos.fetchall()
      if myresult:
         for x in myresult:
            return ("EL CORREO EXISTE")
      else:
          mycursor = mydb.cursor()
          mycursor.execute("INSERT INTO alumnos (Nombre, Correo) VALUES (%s, %s)", (user,mail))
          mydb.commit()
          return ("CORREO AÑADIDO SATISFACTORIAMENTE")
   else:
      return render_template('formulario_addmail.html')