from config.db import criar_conexao

def cadastrar_cliente(nome, email, telefone, senha):
    try:
        conn = criar_conexao()
        if conn is None: return
        
        cursor = conn.cursor()
        query = """INSERT INTO clientes (nome, email, telefone, senha, is_admin) 
                   VALUES (%s, %s, %s, %s, 0)"""
        cursor.execute(query, (nome, email, telefone, senha))
        conn.commit()
        print("✅ Cliente cadastrado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao cadastrar: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def listar_clientes():
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT id_cliente, nome, email, is_admin FROM clientes"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def excluir_cliente(id_cliente):
    """Função nova para o Admin remover um cliente."""
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        
        # Tenta excluir pelo ID
        query = "DELETE FROM clientes WHERE id_cliente = %s"
        cursor.execute(query, (id_cliente,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print("✅ Cliente removido com sucesso!")
        else:
            print("⚠️ Cliente não encontrado.")
            
    except Exception as e:
        print(f"❌ Erro ao excluir: {e}")
        print("Dica: Não é possível excluir clientes que já compraram ingressos (histórico de vendas).")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()