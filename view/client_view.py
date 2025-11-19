from utils import clear_screen, pause, get_int_input
from services.filme_service import listar_filmes
from services.sessao_service import listar_sessoes, listar_sessoes_por_filme
from services.ingresso_service import vender_ingresso, listar_meus_ingressos

def menu_cliente(usuario_logado):
    id_cliente = usuario_logado[0]
    nome_cliente = usuario_logado[1]

    while True:
        clear_screen()
        print(f"=== CINE SYSTEM - Olá, {nome_cliente} ===")
        print("1 - Ver Filmes em Cartaz")
        print("2 - Comprar Ingresso (Novo Fluxo)")
        print("3 - Meus Ingressos")
        print("0 - Sair")

        opcao = get_int_input("\nEscolha: ")

        match opcao:
            case 1:
                filmes = listar_filmes()
                print("\n--- Filmes ---")
                for f in filmes:
                    print(f"ID: {f[0]} | {f[1]} ({f[2]} min) - {f[4]}")
                pause()
            
            case 2:
                # PASSO 1: Escolher o Filme
                filmes = listar_filmes()
                print("\n--- Passo 1: Escolha o Filme ---")
                for f in filmes:
                    print(f"ID: {f[0]} | {f[1]}")
                
                id_filme = get_int_input("\nDigite o ID do Filme desejado: ")

                # PASSO 2: Escolher a Sessão daquele filme
                sessoes = listar_sessoes_por_filme(id_filme)
                
                if not sessoes:
                    print("⚠️ Nenhuma sessão encontrada para este filme.")
                    pause()
                    continue

                print(f"\n--- Passo 2: Sessões para o filme escolhido ---")
                for s in sessoes:
                    # s = (id_sessao, data, numero_sala, capacidade)
                    print(f"ID: {s[0]} | Data: {s[1]} | Sala: {s[2]}")

                id_sessao = get_int_input("\nDigite o ID da Sessão: ")

                # PASSO 3: Escolher Assento e Comprar
                print("\n--- Passo 3: Finalizar Compra ---")
                assento = input("Escolha seu assento (ex: A1): ").strip().upper()
                valor = 25.00 

                confirmar = input(f"Comprar assento {assento} por R$ {valor}? (s/n): ")
                if confirmar.lower() == 's':
                    vender_ingresso(id_cliente, id_sessao, assento, valor)
                else:
                    print("Compra cancelada.")
                pause()

            case 3:
                meus_tickets = listar_meus_ingressos(id_cliente)
                print("\n--- Seus Ingressos ---")
                for t in meus_tickets:
                    print(f"Filme: {t[1]} | Data: {t[3]} | Sala: {t[4]} | Assento: {t[5]}")
                pause()

            case 0:
                break
            case _:
                print("Opção inválida.")