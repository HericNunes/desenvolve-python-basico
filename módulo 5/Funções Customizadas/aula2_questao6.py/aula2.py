
par_ou_impar = lambda x: "par" if x % 2 == 0 else "ímpar"

print("Digite os valores que deseja verificar a paridade (digite 0 para finalizar a entrada de dados):")

while True:
    valor = int(input())
    if valor == 0:
        break
    print(par_ou_impar(valor))
