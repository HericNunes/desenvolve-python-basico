turmas = [
    {'ações comunitárias', 'futebol', 'música', 'rugby'},
    {'ações comunitárias', 'música', 'rugby', 'teatro'},
    {'música', 'rugby', 'teatro', 'vôlei'},
    {'música', 'vôlei', 'rugby'},
    {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'futebol', 'rugby'},
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'rugby', 'vôlei'}
]
comum_a_todas = set.intersection(*turmas)
print("Atividades comuns a todas as turmas:", comum_a_todas)
