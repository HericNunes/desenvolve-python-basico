resultado = int(input())
while True:
    operador = input()
    
    if operador == "Fim":
        break

    numero = int(input())

    if operador == "+":
        resultado += numero
    elif operador == "-":
        resultado -= numero
    else:
        print("Operador inválido!")

print(resultado)
