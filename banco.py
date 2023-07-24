import textwrap


def menu():
    menu = """\n
    =============MENU=============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor> 0: 
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n ===Deposito realizado com sucesso!!===")
    else:
        print("Operação com falha!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    saldo_ins = valor > saldo
    limite_ins = valor > limite
    saques_ins = num_saques >= limite_saques
    if saldo_ins:
            print("Saldo menor que o valor do saque, operação com falha!")
    elif limite_ins:
            print("Operação com falha! Saldo excedeu o limite")
    elif saques_ins:
            print("Voce ja realizou 3 saques hoje, não pode reralizar mais. Falha!")
                    
    elif valor > 0:
            saldo -= valor
            extrato += f"saque R$ {valor:.2f}\n"
            num_saques += 1
    else:
            print("Operação nao realiza, pois formto estava invalido")
    return saldo, extrato
      
def exibir_extrato(saldo, /, *, extrato):
         print("\n====================Extrato=====================")
         print("Nao foram realizadas movimentações." if not extrato else extrato)
         print(f"\n saldo: R$ {saldo:.2f}")
         print("==================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuario nao encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    limite_saques = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu() 
        if opcao == "d":
             valor = float(input("informe o valor do seu deposito: "))
             saldo, extrato = depositar(saldo, valor, extrato,)

        elif opcao == "s":
             valor = float(input("informe o valor do seu saque: "))
             saldo, extrato = sacar(
                   saldo=saldo,
                   valor=valor,
                   extrato=extrato,
                   limite=limite,
                   num_saques=num_saques,
                   limite_saques=limite_saques) 

        elif opcao == "e":
             exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
             criar_usuario(usuarios)
    
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
             listar_contas(contas)
        
        elif opcao == "q":
             break
        else:
         print("Ooeração invalida!!")

main()

