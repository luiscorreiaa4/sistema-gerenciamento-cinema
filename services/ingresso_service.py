from config.db import criar_conexao
import mysql.connector

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

def verificar_assento_ocupado(id_sessao, assento):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT count(*) FROM ingressos WHERE id_sessao = %s AND assento = %s"
        cursor.execute(query, (id_sessao, assento))
        ocupado = cursor.fetchone()[0] > 0
        return ocupado
    except Exception:
        return True
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def vender_ingresso(id_cliente, id_sessao, assento, valor):
    if verificar_lotacao(id_sessao):
        print("❌ Erro: A sessão está LOTADA!")
        return

    if verificar_assento_ocupado(id_sessao, assento):
        print(f"❌ Erro: O assento {assento} já está ocupado!")
        return

    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        
        query = "INSERT INTO ingressos (id_cliente, id_sessao, assento, valor) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (id_cliente, id_sessao, assento, valor))
        conn.commit()
        print("✅ Ingresso vendido com sucesso!")
        
    except mysql.connector.IntegrityError:
        print(f"❌ Erro: O assento {assento} acabou de ser comprado por outra pessoa.")
    except Exception as e:
        print(f"❌ Erro ao vender ingresso: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()
def listar_meus_ingressos(id_cliente):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = """
        SELECT i.id_ingresso, f.titulo, f.classificacao, s.data_hora, sa.numero_sala, i.assento, i.valor
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
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = """
        SELECT i.id_ingresso, c.nome, f.titulo, f.classificacao, sa.numero_sala, i.assento
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