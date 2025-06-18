def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

# Programa principal
n = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado = fatorial(n)
print(f"O fatorial de {n} é {resultado}")