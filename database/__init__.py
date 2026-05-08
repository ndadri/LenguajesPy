from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de la DB
db = SQLAlchemy()

def init_db(app):
    # Unir la base de datos con la aplicacion
    db.init_app(app)

    # Creamos las tablas en la base de datos 
    with app.app_context():
        print("Inicializando la base de datos...") #DEBUG
        from .models import Usuario, Categoria, Libro, Prestamo, Cliente
        
        db.create_all()
        
        print("¡Base de datos creada!") #DEBUG
        