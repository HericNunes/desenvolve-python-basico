def soma_quadrados(a, b):
    return a**2 + b**2
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = soma_quadrados(num1, num2)
print(f"A soma dos quadrados de {num1} e {num2} é {resultado}")