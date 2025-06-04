pontuacao = float(input("Digite a pontuação do jogador: "))
if pontuacao >= 90:
    classificacao = "Excelente"
elif pontuacao >= 80:
    classificacao = "Bom"
elif pontuacao >= 70:
    classificacao = "Regular"
else:
    classificacao = "Insatisfatório"
print(f"Classificação: {classificacao}")
