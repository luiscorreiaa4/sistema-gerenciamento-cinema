from utils import clear_screen, pause, get_int_input
from services.filme_service import listar_filmes
from services.sessao_service import listar_sessoes
from services.ingresso_service import vender_ingresso, listar_meus_ingressos

def menu_cliente(usuario_logado):
    # usuario_logado é uma tupla (id, nome, email, fone, senha) vinda do banco
    id_cliente = usuario_logado[0]
    nome_cliente = usuario_logado[1]

    while True:
        clear_screen()
        print(f"=== BEM-VINDO AO CINEMA, {nome_cliente.upper()} ===")
        print("1 - Ver Filmes em Cartaz")
        print("2 - Ver Sessões Disponíveis")
        print("3 - Comprar Ingresso")
        print("4 - Meus Ingressos")
        print("0 - Sair (Logout)")

        opcao = get_int_input("\nEscolha: ")

        match opcao:
            case 1:
                filmes = listar_filmes()
                print("\n--- Filmes ---")
                for f in filmes:
                    print(f"{f[1]} ({f[4]}) - {f[2]} min")
                pause()
            
            case 2:
                sessoes = listar_sessoes()
                print("\n--- Próximas Sessões ---")
                for s in sessoes:
                    print(f"ID: {s[0]} | {s[1]} | Filme: {s[2]} | Sala: {s[3]}")
                pause()

            case 3:
                print("\n--- Compra de Ingresso ---")
                id_sessao = get_int_input("Digite o ID da Sessão desejada: ")
                assento = input("Escolha seu assento (ex: A1): ")
                # Aqui definimos o preço fixo ou calculamos, vou por fixo pra simplificar
                valor = 25.00 
                print(f"Valor do ingresso: R$ {valor}")
                confirmar = input("Confirmar compra? (s/n): ")
                
                if confirmar.lower() == 's':
                    # Note que passamos o id_cliente logado automaticamente!
                    vender_ingresso(id_cliente, id_sessao, assento, valor)
                else:
                    print("Compra cancelada.")
                pause()

            case 4:
                meus_tickets = listar_meus_ingressos(id_cliente)
                print("\n--- Seus Ingressos ---")
                for t in meus_tickets:
                    # Agora mostra a sala (t[3])
                    print(f"Filme: {t[1]} | Data: {t[2]} | Sala: {t[3]} | Assento: {t[4]}")
                pause()

            case 0:
                break
            case _:
                print("Opção inválida.")