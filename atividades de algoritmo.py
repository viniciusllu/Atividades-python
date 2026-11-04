##Longest Increasing Subsequence (LIS)

sequencia = [10, 22, 9, 33, 21, 50, 41, 60]

dp = [1] * len(sequencia)

for i in range(len(sequencia)):
    for j in range(i):
        if sequencia[j] < sequencia[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

##Longest Increasing Subsequence (LIS)

moedas = [1, 3, 4]
valor = 5

dp = [0] * (valor + 1)
dp[0] = 1

for i in range(1, valor + 1):
    for moeda in moedas:
        if i >= moeda:
            dp[i] += dp[i - moeda]

print(dp[valor])