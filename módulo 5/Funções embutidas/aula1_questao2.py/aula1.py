import random
import math

n = int(input("Digite a quantidade de números a serem gerados: "))

soma = 0

for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor

raiz = math.sqrt(soma)

print("Soma dos valores gerados:", soma)
print("Raiz quadrada da soma:", round(raiz, 2))
