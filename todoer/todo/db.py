import mysql.connector #para trabajan con mysql

import click #es una herramienta para ejecutar comandos en la terminal a traves de comandos
from flask import current_app, g #  mantiene la app ejecutando | guarda las variables para trabajar, especificamente el usuario
from flask.cli import with_appcontext # accederemos a las configuraciones de la aplicacion
from .schema import instructions # contener todos los scrips para crear la base de datos

def get_db(): #para obener los datos de la base de datos
    if 'db' not in g: #si db no esta en g se definiran las siguientes variables
        g.db =mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c=g.db.cursor(dictionary=True) #para acceder a las variables como un diccionario
        return g.db, g.c

#para cerrar la conexion de base de datos al terminar la peticion
def close_db(e=None):#none hace referia a que no tiene valor
    db= g.pop('db',None)#quitar la propiedad de db a g
    if db is not None: #si no tiene none significa que nunca se solicito algo por lo que no es necesario cerrar la conexion
        db.close() #pero si si la tiene definida, tendremos que cerrarla

def init_app(app): #
    app.teardown_appcontext(close_db) #para ejecutar la funcion al termino de ejecutar la peticion