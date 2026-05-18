n = int(input("Fatorial de: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"O fatorial é {fatorial}")