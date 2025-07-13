import random
def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []
    for palavra in palavras:
        if len(palavra) <= 3:
            resultado.append(palavra)
        else:
            primeira = palavra[0]
            ultima = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = primeira + ''.join(meio) + ultima
            resultado.append(nova_palavra)
    return ' '.join(resultado)
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
