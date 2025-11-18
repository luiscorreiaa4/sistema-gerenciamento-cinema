from config.db import criar_conexao

def login_sistema(email, senha):
    conn = criar_conexao()
    if not conn: return None
    
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM clientes WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha))
        
        user = cursor.fetchone()
        return user
    except Exception as e:
        print(f"Erro no login: {e}")
        return None
    finally:
        cursor.close()
        conn.close()