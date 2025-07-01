def ler_lista(n, numero_lista):
    lista = []
    print(f"\nDigite os {n} elementos da lista {numero_lista}:")
    for _ in range(n):
        valor = int(input())
        lista.append(valor)
    return lista

n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = ler_lista(n1, 1)

n2 = int(input("\nDigite a quantidade de elementos da lista 2: "))
lista2 = ler_lista(n2, 2)

intercalada = []
tam = max(n1, n2)

for i in range(tam):
    if i < n1:
        intercalada.append(lista1[i])
    if i < n2:
        intercalada.append(lista2[i])

print("\nLista intercalada:", *intercalada)
