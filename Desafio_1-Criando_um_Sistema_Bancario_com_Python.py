menu = """
===== MENU =====
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
================
=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
opcao = ""
list_dep = [] #lista onde será armazenado todos os depósitos realizados
list_saq = [] #lista onde será armazenado todos os saques realizados

while opcao != "q":

    opcao = input(menu).lower()
    while opcao not in "dseq":
        opcao = input(f"Operação inválida. Por favor selecione novamente a operação desejada.\n{menu}").lower()

    if opcao == "d":
        dep = float(input("Digite quanto deseja depositar:"))
        while dep <= 0:
            dep = float(input(f"Operação Inválida. Digite quanto deseja depositar:"))
        saldo += dep
        list_dep.append(dep)

    elif opcao == "s":
        if numero_saques == 3:
            print("Limite de saques diários atingido")
        else:
            saq = float(input("Digite quanto deseja sacar:"))
            while (saq <= 0 or saq > saldo or saq > 500):
                if saq > saldo:
                    saq = float(input("Saldo insuficiente. Digite novo valor:"))
                elif saq > 500:
                    saq = float(input(f"Valor acima do máximo de R${limite}.00 permitido por saque. Digite novo valor:"))
                else:
                    saq = float(input("Operação Inválida. Digite quanto deseja sacar:"))
            saldo -= saq
            numero_saques += 1
            list_saq.append(saq)
        

    elif opcao == "e":
        print("\n===== EXTRATO =====\n")
        
        print("Depósitos:")
        for i in range(len(list_dep)):
            print(f"R${list_dep[i]:.2f}")
        
        print("\nSaques:")
        for j in range(len(list_saq)):
            print(f"R${list_saq[j]:.2f}")
        
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("================")
    
    else:
        break