n = int(input("Digite o número de jogos do Galo: "))

vitorias = 0
empates = 0
derrotas = 0

for i in range(n):
    gols_galo = int(input(f"Gols do Galo no jogo {i+1}: "))
    gols_oponente = int(input(f"Gols do adversário no jogo {i+1}: "))

    if gols_galo > gols_oponente:
        vitorias += 1
    elif gols_galo == gols_oponente:
        empates += 1
    else:
        derrotas += 1

pontuacao = vitorias * 3 + empates * 1

print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {pontuacao}")
