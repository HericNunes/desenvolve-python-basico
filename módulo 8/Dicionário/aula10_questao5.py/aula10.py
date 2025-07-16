def resultado_votacao(votos):
    totais = {}
    for sessao in votos:
        for candidato, qtd in sessao.items():
            totais[candidato] = totais.get(candidato, 0) + qtd
    total_geral = sum(totais.values())
    resultado = {
        candidato: (total, round((total / total_geral) * 100, 2))
        for candidato, total in totais.items()
    }
    return resultado
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)
