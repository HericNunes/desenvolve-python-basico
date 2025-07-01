def pares_unicos(numeros, soma_objetivo):
    vistos = set()
    pares = set()
    
    for num in numeros:
        complemento = soma_objetivo - num
        if complemento in vistos:
            pares.add(tuple(sorted((num, complemento))))
        vistos.add(num)
    
    return list(pares)

nums = [3, 4, 5, 6, 7]
soma = 10
resultado = pares_unicos(nums, soma)
print(resultado)  
from collections import Counter

lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]

c1 = Counter(lista1)
c2 = Counter(lista2)

diferenca = c1 - c2

resultado = list(diferenca.elements())

print("Diferença entre as listas:", resultado)
