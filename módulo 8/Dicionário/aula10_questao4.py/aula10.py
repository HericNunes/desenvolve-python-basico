def filtrar_dicionario(dicionario, chaves):
    return {chave: dicionario[chave] for chave in chaves if chave in dicionario}
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)
