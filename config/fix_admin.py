from db import criar_conexao
from crypt import hash_password

def atualizar_senha_admin():
    conn = criar_conexao()
    if not conn:
        print("Erro ao conectar")
        return

    try:
        cursor = conn.cursor()
        
        senha_plana = "123"
        senha_hashed = hash_password(senha_plana)
        senha_para_banco = senha_hashed.decode('utf-8')
        
        query = "UPDATE clientes SET senha = %s WHERE email = 'admin@cinema.com'"
        cursor.execute(query, (senha_para_banco,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"✅ Sucesso! A senha do admin foi criptografada.")
            print(f"Nova hash no banco: {senha_para_banco}")
        else:
            print("⚠️ Nenhum admin encontrado com email 'admin@cinema.com'. Verifique o email.")
            
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    atualizar_senha_admin()