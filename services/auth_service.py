from config.db import criar_conexao
from config.crypt import check_password

def login_sistema(email, senha):
    conn = criar_conexao()
    if not conn: return None
    
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM clientes WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        if user and check_password(senha, user[4]):
            return user
    except Exception as e:
        print(f"Erro no login: {e}")
        return None
    finally:
        cursor.close()
        conn.close()