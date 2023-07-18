menu ="""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
num_saques = 0
limite_saques = 3

while True:
    opcao = input(menu) 
    if(opcao == 'd'):
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou, valor informado está incorreto!")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))
        saldo_ins = valor > saldo
        limite_ins = valor > saldo
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
        
    elif opcao == 'e':
        print("\n====================Extrato=====================")
        print("Nao foram realizadas movimentações." if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print("==================================================")
        
    elif opcao == 'q':
        break
    
    else:
        print("Operação invalida selecione novamente a operação desejada")
        