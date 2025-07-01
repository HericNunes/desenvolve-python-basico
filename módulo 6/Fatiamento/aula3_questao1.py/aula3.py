valores = []
print("Digite pelo menos 4 números inteiros (digite 'fim' para encerrar):")

while True:
    entrada = input()
    if entrada.lower() == "fim":
        if len(valores) >= 4:
            break
        else:
            print("Você precisa digitar pelo menos 4 números!")
            continue
    try:
        num = int(entrada)
        valores.append(num)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'fim' para encerrar.")
print("\nLista original:", valores)
print("3 primeiros elementos:", valores[:3])
print("2 últimos elementos:", valores[-2:])
print("Lista invertida:", valores[::-1])
print("Elementos de índice par:", valores[::2])
print("Elementos de índice ímpar:", valores[1::2])
