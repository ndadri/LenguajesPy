import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import init_db

# 1. CARGAR VARIABLES DE ENTORNO
load_dotenv()

app = Flask(__name__)

# 2. CONSTRUCCIÓN DE LA CONFIGURACIÓN (DEBE IR ANTES DE INIT_DB)
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Agregamos +pymysql para usar el driver que instalamos
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 3. INICIALIZACIÓN DE LA BASE DE DATOS
init_db(app)

@app.route("/")
def test_connection():
    return jsonify({
        "status": "online",
        "message": "Configuración de base de datos cargada correctamente",
        "user_connected": DB_USER,
        "database": DB_NAME
    })

if __name__ == '__main__':
    app.run(debug=True)