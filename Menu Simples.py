opcao = -1
while opcao != 0:
    print("1 - Ver produtos | 2 - Ver promoções | 0 - Sair")
    opcao = int(input("Escolha: "))
    if opcao == 1:
        print("Ver produtos...")
    elif opcao == 2:
        print("Ver promoções...")
print("Programa encerrado.")