import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# 1. CARGAMOS VARIABLES DE ENTORNO
load_dotenv()

app = Flask(__name__)

# 2. DATOS DE CONEXION

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')  # Ej: localhost o 127.0.0.1
DB_PORT = os.getenv('DB_PORT')  # Ej: 1433
DB_NAME = os.getenv('DB_NAME')

# 3. URI PARA SQL SERVER (USANDO PYODBC)

SQLALCHEMY_DATABASE_URI = (
    f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_HOST},{DB_PORT}/{DB_NAME}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 4. INSTANCIA DE SQLALCHEMY
db = SQLAlchemy(app)

@app.route("/")
def test_connection():
    return jsonify({
        "status": "online",
        "message": "Configuracion de base de datos SQL Server cargada correctamente",
        "user_connected": DB_USER
    })

if __name__ == "__main__":
    app.run(debug=True) 