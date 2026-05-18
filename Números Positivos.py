contagem = 0
for i in range(5):
    n = int(input("Digite um número: "))
    if n > 0:
        contagem += 1
        print (f"Número positivo: {n}")
    else:
        print(f"Número não é positivo: {n}")
print(f"Quantidade de números positivos: {contagem}")