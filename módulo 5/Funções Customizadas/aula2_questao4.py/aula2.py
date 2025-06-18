def inverteValor(n):
    invertido = 0
    sinal = -1 if n < 0 else 1
    n = abs(n)
    
    while n > 0:
        ultimo_digito = n % 10
        invertido = invertido * 10 + ultimo_digito
        n = n // 10

    return sinal * invertido

def verificaInverso(orig, inv):
    return (orig % 2) == (inv % 2)
valor = int(input("Digite um número inteiro: "))

valor_invertido = inverteValor(valor)
verificacao = verificaInverso(valor, valor_invertido)

print(f"Valor invertido: {valor_invertido}")
print(f"Paridade igual? {verificacao}")
