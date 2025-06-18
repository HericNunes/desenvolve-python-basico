opcao = input("Opções: (1) maior ou (2) menor?\nOpção: ")
operacao = (lambda a, b: a if a > b else b) if opcao == "1" else (lambda a, b: a if a < b else b)

print("\nDigite os valores de entrada. Digite 0 para finalizar a entrada de valores.")
resultado = None

while True:
    valor = int(input())
    if valor == 0:
        break
    if resultado is None:
        resultado = valor
    else:
        resultado = operacao(resultado, valor)
if resultado is not None:
    msg = "maior" if opcao == "1" else "menor"
    print(f"\nO {msg} valor é: {resultado}")
else:
    print("\nNenhum valor foi inserido.")
