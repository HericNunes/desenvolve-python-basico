idade = int(input("Qual é a sua idade? "))
ja_jogou_3 = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True/False) ")
vitorias = int(input("Quantas vezes você venceu um jogo? "))

ja_jogou_3 = ja_jogou_3.strip().lower() == "true"
pode_entrar = (16 <= idade <= 18) and ja_jogou_3 and (vitorias >= 1)
print(pode_entrar)