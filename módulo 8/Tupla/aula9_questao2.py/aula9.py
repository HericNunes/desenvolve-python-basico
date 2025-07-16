frase = "O rato roeu a roupa da Alice"
vogais = "aeiouAEIOU"
vogais_encontradas = []
indices = []
for i, letra in enumerate(frase):
    if letra in vogais:
        vogais_encontradas.append(letra)
        indices.append(i)
print("Vogais encontradas:", vogais_encontradas)
print("Índices:", indices)
