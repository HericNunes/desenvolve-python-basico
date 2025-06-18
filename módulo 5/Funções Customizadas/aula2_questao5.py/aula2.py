import math

def calcula_perimetro_triangulo(a, b, c):
    return a + b + c

def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio

def calcula_perimetro_retangulo(lado1, lado2=0):
    if lado2 == 0:
        return 4 * lado1  # Quadrado
    else:
        return 2 * (lado1 + lado2)  # Retângulo
while True:
    print("\n1 - Calcular perímetro triângulo")
    print("2 - Calcular perímetro círculo")
    print("3 - Calcular perímetro retângulo")
    print("4 - Sair")
    
    opcao = input("Opção: ")

    if opcao == "1":
        print("Digite os três lados do triângulo:")
        a = int(input("Lado 1: "))
        b = int(input("Lado 2: "))
        c = int(input("Lado 3: "))
        perimetro = calcula_perimetro_triangulo(a, b, c)
        print(f"O perímetro é: {perimetro}")

    elif opcao == "2":
        raio = float(input("Digite o raio do círculo: "))
        perimetro = calcula_perimetro_circulo(raio)
        print(f"O perímetro é: {perimetro:.2f}")

    elif opcao == "3":
        print("Informe os dois lados do retângulo. Se for um quadrado, digite 0 para o segundo valor:")
        lado1 = int(input("Lado 1: "))
        lado2 = int(input("Lado 2: "))
        perimetro = calcula_perimetro_retangulo(lado1, lado2)
        print(f"O perímetro é: {perimetro}")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")