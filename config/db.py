import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'database': 'cinema_db',
    'user': 'root',
    'password': '150904',
    'host': 'localhost',
    'port': '3306'
}

def criar_conexao():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Erro ao conectar com o banco de dados MySQL: {e}")
        return None