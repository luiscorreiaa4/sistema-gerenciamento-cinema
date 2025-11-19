from config.db import criar_conexao

def cadastrar_sessao(data_hora: str, id_filme: int, id_sala: int):
    try:
        conn = criar_conexao()
        if conn is None: return

        cursor = conn.cursor()
        query = "INSERT INTO sessoes (data_hora, id_filme, id_sala) VALUES (%s, %s, %s)"
        cursor.execute(query, (data_hora, id_filme, id_sala))
        conn.commit()
        print("Sessão agendada com sucesso!")

    except Exception as e:
        print(f"Erro ao agendar sessão: {e}")
        print("Dica: Verifique se o ID do filme e da Sala existem.")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def listar_sessoes():
    try:
        conn = criar_conexao()
        if conn is None: return []

        cursor = conn.cursor()
        
        query = """
        SELECT s.id_sessao, s.data_hora, f.titulo, sa.numero_sala 
        FROM sessoes s
        JOIN filmes f ON s.id_filme = f.id_filme
        JOIN salas sa ON s.id_sala = sa.id_sala
        """
        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print(f"Erro ao listar sessões: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()
def listar_sessoes_por_filme(id_filme):
    try:
        conn = criar_conexao()
        if conn is None: return []
        cursor = conn.cursor()
        
        query = """
        SELECT s.id_sessao, s.data_hora, sa.numero_sala, sa.capacidade
        FROM sessoes s
        JOIN salas sa ON s.id_sala = sa.id_sala
        WHERE s.id_filme = %s
        """
        cursor.execute(query, (id_filme,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar sessões do filme: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()