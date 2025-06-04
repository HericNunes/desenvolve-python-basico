num1 = float(input("Digite o primeiro operando: "))
operador = input("Digite o operador (+, -, /, *, **): ").strip()
num2 = float(input("Digite o segundo operando: "))
if operador == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro! Divisão por zero.")
elif operador == "**":
    resultado = num1 ** num2
    print(f"Resultado: {num1} ** {num2} = {resultado}")
else:
    print("Erro! Operação inválida.")
