import time
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
NUMERO_AGENCIA = "0001"
numero_conta = 1

def sacar(*, saldo: float, valor: float, extrato: str, limite: float, numero_saques: int, LIMITE_SAQUES: int):
    if valor > saldo:
        print("Operação falhou!, Você tem saldo suficiente.")
        return saldo, extrato
    if valor > limite:
        print("Operação falhou! O valor do saque exced o limite.")
        return saldo, extrato
    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato
    if valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def depositar(saldo: float, calor: float, extrato: str):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor inforamdo é inválido)")
    return saldo, extrato

def show_extrato(saldo: float, *, extrato: str):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def crar_usuario(nome: str, data_nascimento: str, cpf:str, endereco: str):
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro: Já existe um usuário com este CPF.")
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf.replace(".", "").replace("-", ""),
        'endereco': endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

def criar_conta_corrente(usuario_cpf: str):
    global numero_conta
    usuario = next((u for u in usuarios if u['cpf'] == usuario_cpf), None)
    if usuario is None:
        print("Erro: Usuário não encontrado.")
        return
    conta = {
        'agencia': NUMERO_AGENCIA,
        'numero': numero_conta,
        'usuario' : usuario
    }
    contas.append(conta)
    numero_conta += 1
    print(f"Conta corrente {conta['numero']} criada para o usuário {usuario['nome']} com sucesso!")

def listar_contas():
    if not contas:
        print("Não há contas cadastradas.")
        return
    for conta in contas:
        usuario = conta['usuario']
        print(f"Ag~encia: {conta['agencia']} | Conta: {conta['nuemro']} | Nome: {usuario['nome']}")

def get_time():
    
    pass #retorna a hora

def menu_bancario():

    global saldo, limite, extrato, nuemro_saques, LIMITE_SAQUES

    while True:

        menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[n] Criar Conta Corrente
[l] Listar Contas
[q] Sair

=> """

        opcao = input(menu)

        if opcao == "d":
        
            try:
                valor = float(input("Informe o valor do depósito: "))

                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                   numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
            except ValueError:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":

            try:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                       numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

            except ValueError:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            show_extrato(saldo, extrato=extrato)

        elif opcao == "c":
            nome = input("Nome do usuário: ")
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (apenas números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla do estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "n":
            cpf = input("CPF do usuário para criar conta (apenas números): ")
            criar_conta_corrente(cpf)

        elif opcao == "l":
            listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

menu_bancario()