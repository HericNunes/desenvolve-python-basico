def comprimir_tuplas(lista):
    dicionario = {}
    for palavra, numero in lista:
        if palavra in dicionario:
            dicionario[palavra] += numero
        else:
            dicionario[palavra] = numero
    return list(dicionario.items())
tuplas_originais = [('maçã', 3), ('banana', 2), ('maçã', 5), ('laranja', 1), ('banana', 3)]
resultado = comprimir_tuplas(tuplas_originais)
print(resultado)
