#para empezar a trabajar con flask, muchas veces nos aparecere flask en amarillo pero es normal
import email
from flask import Flask,request, url_for, redirect, abort, render_template
app =Flask(__name__)

import mysql.connector
midb=mysql.connector.connect(
    host="localhost",
    user="gerardo.heredia",
    password="Here182615",
    database="prueba"
)



cursor=midb.cursor(dictionary=True) #con dictionary= True tendremos los encabezados de la columna



#para crear rutas

@app.route('/')
def index():
    return 'hola mundo'
#GET, POST,PUT(remplazar un recurso),PATCH (modificar un recurso parcialmete),DELETE son los mas ocupados en rest
#para pasar los metodos se puede realizar de la siguiente manera
@app.route('/post/<post_id>',methods=['GET','POST']) #para forzar que el numero del id sea un entero hay que ocupar int
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este es otro método y no GET'

@app.route('/lele', methods=['POST','GET'])
def lele():
    cursor.execute('select * from Usuario')
    usuarios=cursor.fetchall()
    #abort (403)
    #return redirect (url_for('lala',post_id=2))#hay que mandar el valor post cuando se ocupe otra funcion
    # print (request.form)
    # print (request.form['llave1'])
    #return render_template('lele.html') #para regresar objetos html
    # return { #regresar json, se pueden ocupar con las APIREST
    #     "username":'gerardo.heredia',
    #     "email":'carlos.valenzh@gmail.com'
    # }
    return render_template('lele.html',usuarios=usuarios) #la data sera el resultado de la consulta, pero lo cambiaremos a usuarios
    # para que se haga mas facil el manejo, se cambia el del color naranja

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html',mensaje='Hola mundo')

@app.route('/crear',methods=['GET','POST'])
def crear():
    if request.method=="POST":
        username=request.form['username']
        email = request.form['email']
        sql= "insert into Usuario (username,email) values (%s, %s)"
        values = (username,email)
        cursor.execute(sql,values)
        midb.commit()

        return redirect(url_for('lele'))

    return render_template('crear.html')