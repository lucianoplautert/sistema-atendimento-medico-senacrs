import funcoes


def exibir_menu():
    print("\n=========================================")
    print(" SISTEMA DE GERENCIAMENTO DE ATENDIMENTO")
    print("=========================================")
    print("1 - Cadastro Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastro Especialista")
    print("4 - Listar Especialista")
    print("5 - Cadastrar Novo Atendimento")
    print("6 - Verificar Atendimentos")
    print("7 - Exportar Dados (CSV)")
    print("8 - Importar Dados (CSV)")
    print("0 - Sair")
    print("=========================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            funcoes.cadastrar_cliente()
        elif opcao == "2":
            funcoes.listar_clientes()
        elif opcao == "3":
            funcoes.cadastrar_especialista()
        elif opcao == "4":
            funcoes.listar_especialistas()
        elif opcao == "5":
            funcoes.cadastrar_atendimento()
        elif opcao == "6":
            funcoes.verificar_atendimentos()
        elif opcao == "7":
            funcoes.exportar_dados()
        elif opcao == "8":
            funcoes.importar_dados()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()