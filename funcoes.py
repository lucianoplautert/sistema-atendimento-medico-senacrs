import csv
import os

# Listas para armazenar os dados em memória
clientes = []
especialistas = []
atendimentos = []


def cadastrar_cliente():
    print("\n--- CADASTRO DE CLIENTE ---")
    nome = input("Nome do cliente: ").strip()
    contato = input("Telefone / CPF: ").strip()

    if not nome:
        print("Aviso: o nome do cliente é obrigatório.")
        return

    clientes.append({"nome": nome, "contato": contato})
    print(f"Cliente '{nome}' cadastrado com sucesso!")


def listar_clientes():
    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for i, c in enumerate(clientes, start=1):
        print(f"{i}. {c['nome']} | Contato: {c['contato']}")


def cadastrar_especialista():
    print("\n--- CADASTRO DE ESPECIALISTA ---")
    nome = input("Nome do especialista: ").strip()
    especialidade = input("Especialidade / Tipo de Serviço: ").strip()

    if not nome or not especialidade:
        print("Aviso: informe o nome e a especialidade.")
        return

    especialistas.append({"nome": nome, "especialidade": especialidade})
    print(f"Especialista '{nome}' cadastrado com sucesso!")


def listar_especialistas():
    print("\n--- LISTA DE ESPECIALISTAS ---")
    if not especialistas:
        print("Nenhum especialista cadastrado.")
        return

    for i, e in enumerate(especialistas, start=1):
        print(f"{i}. {e['nome']} | Serviço: {e['especialidade']}")


def cadastrar_atendimento():
    print("\n--- CADASTRAR NOVO ATENDIMENTO ---")
    if not clientes:
        print("Aviso: cadastre ao menos um cliente primeiro.")
        return

    print("Clientes disponíveis:")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. {c['nome']}")

    try:
        indice = int(input("Escolha o número do cliente: ")) - 1
        cliente_escolhido = clientes[indice]["nome"]
    except (ValueError, IndexError):
        print("Opção de cliente inválida.")
        return

    if especialistas:
        servicos = list({e["especialidade"] for e in especialistas})
        print("Serviços cadastrados:", ", ".join(servicos))

    servico = input("Tipo de serviço: ").strip()
    horario = input("Horário (ex: 14:30 - 25/11): ").strip()

    if not servico or not horario:
        print("Aviso: serviço e horário são obrigatórios.")
        return

    atendimentos.append({
        "servico": servico,
        "cliente": cliente_escolhido,
        "horario": horario,
    })
    print("Atendimento agendado com sucesso!")


def verificar_atendimentos():
    print("\n--- VERIFICAR ATENDIMENTOS ---")
    if not atendimentos:
        print("Nenhum atendimento agendado até o momento.")
        return

    print(f"{'TIPO DE SERVIÇO':<22} | {'CLIENTE':<22} | {'HORÁRIO'}")
    print("-" * 65)
    for a in atendimentos:
        print(f"{a['servico']:<22} | {a['cliente']:<22} | {a['horario']}")


def exportar_dados():
    print("\n--- EXPORTAR DADOS PARA CSV ---")
    
    try:
        # Exporta Clientes
        with open("clientes.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nome", "contato"])
            writer.writeheader()
            writer.writerows(clientes)

        # Exporta Especialistas
        with open("especialistas.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nome", "especialidade"])
            writer.writeheader()
            writer.writerows(especialistas)

        # Exporta Atendimentos
        with open("atendimentos.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["servico", "cliente", "horario"])
            writer.writeheader()
            writer.writerows(atendimentos)

        print("Dados exportados com sucesso para arquivos CSV (clientes.csv, especialistas.csv, atendimentos.csv)!")
    except OSError as e:
        print(f"Erro ao exportar dados em CSV: {e}")


def importar_dados():
    print("\n--- IMPORTAR DADOS DE CSV ---")

    lidos_clientes = []
    lidos_especialistas = []
    lidos_atendimentos = []

    # Leitura de Clientes
    if os.path.exists("clientes.csv"):
        try:
            with open("clientes.csv", "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                lidos_clientes = list(reader)
        except OSError as e:
            print(f"Erro ao ler clientes.csv: {e}")
    else:
        print("Arquivo 'clientes.csv' não encontrado.")

    # Leitura de Especialistas
    if os.path.exists("especialistas.csv"):
        try:
            with open("especialistas.csv", "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                lidos_especialistas = list(reader)
        except OSError as e:
            print(f"Erro ao ler especialistas.csv: {e}")
    else:
        print("Arquivo 'especialistas.csv' não encontrado.")

    # Leitura de Atendimentos
    if os.path.exists("atendimentos.csv"):
        try:
            with open("atendimentos.csv", "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                lidos_atendimentos = list(reader)
        except OSError as e:
            print(f"Erro ao ler atendimentos.csv: {e}")
    else:
        print("Arquivo 'atendimentos.csv' não encontrado.")

    # Atualiza as listas em memória
    clientes.clear()
    clientes.extend(lidos_clientes)
    especialistas.clear()
    especialistas.extend(lidos_especialistas)
    atendimentos.clear()
    atendimentos.extend(lidos_atendimentos)

    print(
        f"Importação concluída! "
        f"({len(clientes)} clientes, {len(especialistas)} especialistas, {len(atendimentos)} atendimentos)"
    )