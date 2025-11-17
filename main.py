import getpass
from utils import clear_screen, pause, get_int_input
from services.auth_service import login_sistema
from services.cliente_service import cadastrar_cliente
from view.admin_view import menu_principal as menu_admin
from view.client_view import menu_cliente

def main():
    while True:
        clear_screen()
        print("--- CINE SYSTEM ---")
        print("1 - Entrar (Login)")
        print("2 - Criar Conta")
        print("0 - Sair")
        
        opcao = get_int_input("Opção: ")

        match opcao:
            case 1:
                email = input("Email: ")
                senha = getpass.getpass("Senha: ")
                
                usuario_logado = login_sistema(email, senha)
                
                if usuario_logado:
                    # CORREÇÃO: Mudamos de [6] para [5]
                    is_admin = usuario_logado[5] 
                    
                    # O banco retorna 1 para True e 0 para False
                    if is_admin == 1:
                        menu_admin()
                    else:
                        menu_cliente(usuario_logado)
                else:
                    print("❌ Email ou senha incorretos.")
                    pause()

            case 2:
                print("\n--- Cadastro ---")
                nome = input("Nome completo: ")
                email = input("Email: ")
                fone = input("Telefone: ")
                senha = getpass.getpass("Crie sua Senha: ")
                
                cadastrar_cliente(nome, email, fone, senha)
                pause()

            case 0:
                print("Até logo!")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()