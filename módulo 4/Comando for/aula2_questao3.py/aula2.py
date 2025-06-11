print("Digite 10 números positivos:")

soma = 0

for i in range(10):
    numero = int(input())
    soma += numero

media = soma / 10

print(f"A média dos valores digitados é {media:.2f}")