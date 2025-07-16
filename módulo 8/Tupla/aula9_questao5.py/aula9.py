fila = []
while True:
    nome = input("Digite o nome (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    idade = int(input("Digite a idade: "))
    fila.append((nome, idade))
menores = []
maiores = []

for nome, idade in fila:
    if idade < 18:
        menores.append(nome)
    else:
        maiores.append(nome)
tupla_menores = tuple(menores)
tupla_maiores = tuple(maiores)
print("\nMenores de idade (não entram):", tupla_menores)
print("Maiores de idade (podem entrar):", tupla_maiores)
