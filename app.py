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
def login():
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
      return render_template('formulario.html')