import random
from collections import Counter
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(set(lista1) & set(lista2))

contagem1 = Counter(lista1)
contagem2 = Counter(lista2)

print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", interseccao)
print("\nContagem")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem1[elemento]}, lista2={contagem2[elemento]})")
