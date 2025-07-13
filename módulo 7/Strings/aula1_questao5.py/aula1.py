frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU" 
indices_vogais = []

for i, letra in enumerate(frase):
    if letra in vogais:
        indices_vogais.append(i)

print(f"{len(indices_vogais)} vogais")
print(f"Índices {indices_vogais}")