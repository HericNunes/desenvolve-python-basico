def contagem_caracteres(texto):
    contagem = {}
    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem
frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)
