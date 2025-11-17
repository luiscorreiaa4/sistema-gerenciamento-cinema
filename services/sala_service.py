from config.db import criar_conexao

def cadastrar_sala(numero_sala: int, capacidade: int):
    try:
        conn = criar_conexao()
        if conn is None: return

        cursor = conn.cursor()
        query = "INSERT INTO salas (numero_sala, capacidade) VALUES (%s, %s)"
        cursor.execute(query, (numero_sala, capacidade))
        conn.commit()
        print("Sala cadastrada com sucesso!")

    except Exception as e:
        print(f"Erro ao cadastrar sala: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def listar_salas():
    try:
        conn = criar_conexao()
        if conn is None: return []

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salas")
        return cursor.fetchall()

    except Exception as e:
        print(f"Erro ao listar salas: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()