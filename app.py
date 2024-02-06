from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

diccionario = {
        "Mercedes": "mcast386@xtec.cat",
        "Rayane": "rayane@rayane.sa",
        "Mohamed": "moha@gmail.com",
        "Jad": "jad@gmail.com",
        "Oriol": "joam@gmail.com",
        "Elias": "hola123@gmail.com",
        "Armau": "arnau@gmail.com",
        "Asdrúbal": "asdrubal@gmail.com",
        "Adrian": "pedrosanchez@asix2.com",
        "Emma": "pacosanz@gmail.com",
        "nishwan": "nishwan@gmail.com",
        "Javi": "javi@gmail.com",
        "Novel": "novelferreras49@gmail.com",
        "Bruno": "elcigala@gmail.com",
        "David": "argentino@gmail.com",
        "Judit": "judit@gmail.com",
        "Joao": "joao@gmail.com",
        "Laura": "laura@gmail.com",
        "enrico": "123@gmail.com",
        "Joel": "joelcobre@gmail.com",
        "Aaron": "aaron@gmail.com",
        "Moad": "moad@gmail.com",
        }

@app.route('/getmail',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      if user in diccionario:
         mail=diccionario[user]
         return render_template('resultado.html',mail=mail,user=user)
      else:
         return ("NO ENCONTRADO")
   else:
      return render_template('formulario.html')