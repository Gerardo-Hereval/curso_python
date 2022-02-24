import os

from flask import Flask

def create_app():
    app=Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )
    from . import db #importar todo db
    db.init_app(app) #ejecutar la funcion al termino de app 

    @app.route('/hola')
    def hola():
        return 'Hola mundo'
    
    return app