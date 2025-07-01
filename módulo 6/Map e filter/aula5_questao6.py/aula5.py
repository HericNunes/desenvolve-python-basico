import random
lista = [random.randint(1,100) for i in range(20)]

print("Lista original:")
print(lista)

while True:
    tamanho = int(input("\nDigite o tamanho da divisão (0 para sair): "))
    if tamanho == 0:
        print("Programa encerrado.")
        break
    
    sublistas = []
    for i in range(0, len(lista), tamanho):
        sublistas.append(lista[i:i+tamanho])
    
    print("Sublistas:")
    print(sublistas)
