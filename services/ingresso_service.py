from config.db import criar_conexao

def verificar_lotacao(id_sessao):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        
        query_cap = """
        SELECT sa.capacidade FROM sessoes s
        JOIN salas sa ON s.id_sala = sa.id_sala
        WHERE s.id_sessao = %s
        """
        cursor.execute(query_cap, (id_sessao,))
        resultado = cursor.fetchone()
        if not resultado: return True
        capacidade = resultado[0]
        
        query_count = "SELECT COUNT(*) FROM ingressos WHERE id_sessao = %s"
        cursor.execute(query_count, (id_sessao,))
        vendidos = cursor.fetchone()[0]
        
        return vendidos >= capacidade

    except Exception as e:
        print(f"Erro ao verificar lotação: {e}")
        return True
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def vender_ingresso(id_cliente: int, id_sessao: int, assento: str, valor: float):
    if verificar_lotacao(id_sessao):
        print("Erro: A sessão está LOTADA!")
        return

    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        
        query = "INSERT INTO ingressos (id_cliente, id_sessao, assento, valor) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (id_cliente, id_sessao, assento, valor))
        conn.commit()
        print("Ingresso vendido com sucesso!")
        
    except Exception as e:
        print(f"Erro ao vender ingresso: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def listar_meus_ingressos(id_cliente):
    """Para o cliente comum ver seus tickets com a sala."""
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = """
        SELECT i.id_ingresso, f.titulo, s.data_hora, sa.numero_sala, i.assento, i.valor
        FROM ingressos i
        JOIN sessoes s ON i.id_sessao = s.id_sessao
        JOIN filmes f ON s.id_filme = f.id_filme
        JOIN salas sa ON s.id_sala = sa.id_sala
        WHERE i.id_cliente = %s
        """
        cursor.execute(query, (id_cliente,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def listar_todos_ingressos():
    """Para o admin."""
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = """
        SELECT i.id_ingresso, c.nome, f.titulo, sa.numero_sala, i.assento
        FROM ingressos i
        JOIN clientes c ON i.id_cliente = c.id_cliente
        JOIN sessoes s ON i.id_sessao = s.id_sessao
        JOIN filmes f ON s.id_filme = f.id_filme
        JOIN salas sa ON s.id_sala = sa.id_sala
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()