def soma_digitos(n):
    soma = 0
    n = abs(n) 
    while n > 0:
        soma += n % 10     
        n = n // 10        
    return soma

numero = int(input("Digite um número inteiro: "))
resultado = soma_digitos(numero)
print(f"A soma dos dígitos de {numero} é {resultado}")
