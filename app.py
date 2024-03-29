from flask import Flask, session
from flask import render_template
from flask import request
import mysql.connector
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
app.secret_key = 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="aplicaciones_web"
)

@app.route('/',methods = ['POST', 'GET'])
def getmail_redirect():
      return render_template('formulario_getmail.html')


@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      mail = request.form['mail']
      mycursos = mydb.cursor()
      mycursos.execute("SELECT Correo FROM alumnos WHERE Correo = %s",(mail,))
      myresult = mycursos.fetchall()
      if myresult:
         fila = myresult[0]
         correo = fila[0]
         if correo == mail:
            session['mail'] = mail
            return render_template('principal.html', mail=mail)
      else:
         error = 'El correo electrónico es inválido.'
         return render_template('formulario_getmail.html', error=error)
   else:
      return render_template('formulario_getmail.html')

@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      password = request.form['password']
      mail = request.form['mail']
      mycursos = mydb.cursor()
      mycursos.execute("SELECT Correo FROM alumnos WHERE Correo = %s",(mail,))
      myresult = mycursos.fetchall()
      if myresult:
         fila = myresult[0]
         correo = fila[0]
         if correo == mail:
            session['mail'] = mail
            error = 'El correo existe'
            return render_template('crear_mail.html', error=error)
      else:
          mycursor = mydb.cursor()
          mycursor.execute("INSERT INTO alumnos (Contraseña, Correo) VALUES (%s, %s)", (password,mail))
          mydb.commit()
          correcto = 'El correo se ha añadido satisfactoriamente'
          return render_template('formulario_getmail.html', correcto=correcto)
   else:
      return render_template('crear_mail.html')

@app.route('/adopcion',methods = ['POST', 'GET'])
def adopcion():
   if session.get('mail'):
      if request.method == 'POST':
         name = request.form['name']
         surname1 = request.form['surname1']
         surname2 = request.form['surname2']
         number = request.form['number']
         mail = request.form['mail']
         address = request.form['address']
         comments = request.form['comments']
         mycursos = mydb.cursor()
         mycursos.execute("SELECT Correo FROM alumnos WHERE Correo = %s",(mail,))
         myresult = mycursos.fetchall()
         if myresult:
            fila = myresult[0]
            correo = fila[0]
            if correo == mail:
               mycursor = mydb.cursor()
               mycursor.execute("INSERT INTO adopcion (name, surname1, surname2, number, mail, address, comments) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name,surname1,surname2,number,mail,address,comments))
               mydb.commit()
               correcto = "Se ha enviado correctamente el formulario"
               return render_template('adopcion.html',correcto=correcto)
         else:
            error = 'El correo electrónico no existe'
            return render_template('adopcion.html', error=error)
      else:
         return render_template('adopcion.html')
   else:
      return render_template('formulario_getmail.html')

@app.route('/principal',methods = ['POST', 'GET'])
def principal():
   if session.get('mail'):
      return render_template('principal.html')
   else:
      return render_template('formulario_getmail.html')

@app.route('/about',methods = ['POST', 'GET'])
def about():
   if session.get('mail'):
      return render_template('about.html')
   else:
      return render_template('formulario_getmail.html')

@app.route("/ex1",methods = ['POST', 'GET'])
def ex1():
    if session.get('mail'):
      if request.method == 'POST':
         num = int(request.form['num'])
         if num % 2 == 0:
            return ("El nombre es par")
         else:
            return ("El nombre es impar")
      else:
         return render_template('ex1.html')
    else:
      return render_template('formulario_getmail.html')

@app.route("/ex2",methods = ['POST', 'GET'])
def ex2():
   if session.get('mail'):
      if request.method == 'POST':
         edad = int(request.form['edad'])
         edad = 100 - edad
         anyo = int (edad + 2024)
         return ("Cumpliar 100 años el año " + str(anyo))
      else:
         return render_template('ex2.html')
   else:
      return render_template('formulario_getmail.html')

#@app.route('/logout')
#def logoout():
#   if session.get('mail'):
#      session.pop('mail', default=None)
#   return redirect(url_for('formulario_getmail.html'))
   
   