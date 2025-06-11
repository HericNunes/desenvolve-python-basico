n = int(input("Qual a quantidade de respondentes: "))

soma_idades = 0

for i in range(n):
    idade = int(input(f"Digite a idade do respondente {i + 1}: "))
    soma_idades += idade

media = soma_idades / n

print(f"Média das idades: {media:.2f}")
