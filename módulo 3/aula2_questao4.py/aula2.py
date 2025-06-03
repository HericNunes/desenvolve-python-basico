classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ").strip().lower()
forca = int(input("Digite os pontos de Força: "))
magia = int(input("Digite os pontos de Magia: "))
if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    valido = (forca > 5 and forca <= 15) and (magia > 5 and magia <= 15)
else:
    valido = False
print(valido)