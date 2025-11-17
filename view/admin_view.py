from utils import clear_screen, pause, get_int_input
from services.cliente_service import listar_clientes, excluir_cliente
from services.filme_service import cadastrar_filme, listar_filmes
from services.sala_service import cadastrar_sala, listar_salas
from services.sessao_service import cadastrar_sessao, listar_sessoes
from services.ingresso_service import vender_ingresso, listar_todos_ingressos

def sub_menu_clientes():
    while True:
        clear_screen()
        print("--- GESTÃO DE CLIENTES ---")
        print("1 - Listar Clientes")
        print("2 - Excluir Cliente")
        print("0 - Voltar")
        
        opcao = get_int_input("Opção: ")
        
        match opcao:
            case 1:
                clientes = listar_clientes()
                print("\n--- Lista de Clientes ---")
                for c in clientes:
                    tipo = "ADMIN" if c[3] == 1 else "Cliente"
                    print(f"ID: {c[0]} | {c[1]} | {c[2]} | [{tipo}]")
                pause()
                
            case 2:
                print("\n(Dica: Liste primeiro para saber o ID)")
                try:
                    id_alvo = get_int_input("Digite o ID do cliente para excluir: ")
                    confirmar = input(f"Tem certeza que deseja apagar o ID {id_alvo}? (s/n): ")
                    
                    if confirmar.lower() == 's':
                        excluir_cliente(id_alvo)
                    else:
                        print("Operação cancelada.")
                except Exception as e:
                    print("Erro no input.")
                pause()
                
            case 0:
                break
            case _:
                print("Opção inválida.")
                pause()

def sub_menu_filmes():
    while True:
        clear_screen()
        print("--- GESTÃO DE FILMES ---")
        print("1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("0 - Voltar")
        
        opcao = get_int_input("Opção: ")
        
        match opcao:
            case 1:
                titulo = input("Título: ")
                duracao = get_int_input("Duração (minutos): ")
                classificacao = input("Classificação (ex: 14 anos): ")
                genero = input("Gênero: ")
                cadastrar_filme(titulo, duracao, classificacao, genero)
                pause()
            case 2:
                filmes = listar_filmes()
                print("\n--- Catálogo de Filmes ---")
                for f in filmes:
                    print(f"ID: {f[0]} | Título: {f[1]} | {f[2]} min | {f[4]}")
                pause()
            case 0:
                break

def sub_menu_salas():
    while True:
        clear_screen()
        print("--- GESTÃO DE SALAS ---")
        print("1 - Cadastrar Sala")
        print("2 - Listar Salas")
        print("0 - Voltar")
        
        opcao = get_int_input("Opção: ")
        
        match opcao:
            case 1:
                numero = get_int_input("Número da Sala: ")
                cap = get_int_input("Capacidade Máxima: ")
                cadastrar_sala(numero, cap)
                pause()
            case 2:
                salas = listar_salas()
                print("\n--- Salas Disponíveis ---")
                for s in salas:
                    print(f"ID: {s[0]} | Sala {s[1]} | Cap: {s[2]} pessoas")
                pause()
            case 0:
                break

def sub_menu_sessoes():
    while True:
        clear_screen()
        print("--- AGENDAMENTO DE SESSÕES ---")
        print("1 - Criar Nova Sessão")
        print("2 - Ver Sessões Agendadas")
        print("0 - Voltar")
        
        opcao = get_int_input("Opção: ")
        
        match opcao:
            case 1:
                print("\n(Dica: Veja os IDs em Listar Filmes/Salas antes)")
                id_filme = get_int_input("ID do Filme: ")
                id_sala = get_int_input("ID da Sala: ")
                data = input("Data e Hora (AAAA-MM-DD HH:MM:SS): ")
                cadastrar_sessao(data, id_filme, id_sala)
                pause()
            case 2:
                sessoes = listar_sessoes()
                print("\n--- Sessões ---")
                for s in sessoes:
                    # s[0]=id, s[1]=data, s[2]=titulo_filme, s[3]=num_sala
                    print(f"ID: {s[0]} | Data: {s[1]} | Filme: {s[2]} | Sala: {s[3]}")
                pause()
            case 0:
                break

def sub_menu_ingressos():
    while True:
        clear_screen()
        print("--- BILHETERIA ---")
        print("1 - Vender Ingresso")
        print("2 - Histórico de Vendas")
        print("0 - Voltar")
        
        opcao = get_int_input("Opção: ")
        
        match opcao:
            case 1:
                print("\n--- Venda ---")
                id_cli = get_int_input("ID do Cliente: ")
                id_ses = get_int_input("ID da Sessão: ")
                assento = input("Assento (ex: A1, B2): ")
                valor = float(input("Valor (R$): "))
                vender_ingresso(id_cli, id_ses, assento, valor)
                pause()
            case 2:
                vendas = listar_todos_ingressos()
                print("\n--- Ingressos Vendidos ---")
                for v in vendas:
                    print(f"Ticket #{v[0]} | Cliente: {v[1]} | Filme: {v[2]} | Assento: {v[3]}")
                pause()
            case 0:
                break

def menu_principal():
    while True:
        clear_screen()
        print("============================")
        print("   SISTEMA DE CINEMA   ")
        print("============================")
        print("1. Clientes")
        print("2. Filmes")
        print("3. Salas")
        print("4. Sessões (Agendamento)")
        print("5. Ingressos (Vendas)")
        print("0. Sair")
        
        try:
            opcao = int(input("\nEscolha um módulo: "))
        except ValueError:
            continue

        match opcao:
            case 1: sub_menu_clientes()
            case 2: sub_menu_filmes()
            case 3: sub_menu_salas()
            case 4: sub_menu_sessoes()
            case 5: sub_menu_ingressos()
            case 0: 
                print("Saindo...")
                break
            case _: print("Opção inválida!")