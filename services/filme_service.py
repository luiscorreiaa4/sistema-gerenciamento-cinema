from config.db import criar_conexao

def cadastrar_filme(titulo: str, duracao: int, classificacao: str, genero: str):
    try:
        conn = criar_conexao()
        if conn is None: return

        cursor = conn.cursor()
        query = "INSERT INTO filmes (titulo, duracao, classificacao, genero) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (titulo, duracao, classificacao, genero))
        conn.commit()
        print("Filme cadastrado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao cadastrar filme: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def listar_filmes():
    try:
        conn = criar_conexao()
        if conn is None: return []

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM filmes")
        return cursor.fetchall()

    except Exception as e:
        print(f"Erro ao listar filmes: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()