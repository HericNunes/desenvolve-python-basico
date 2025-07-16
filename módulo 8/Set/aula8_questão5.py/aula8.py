import string
def checa_panagrama(frase):
    alfabeto = set(string.ascii_lowercase)
    letras_na_frase = set(c.lower() for c in frase if c.isalpha())
    return letras_na_frase >= alfabeto  
frase1 = "The quick brown fox jumps over the lazy dog"
frase2 = "Python é uma linguagem de programação"
print("É um panagrama" if checa_panagrama(frase1) else "Não é um panagrama")
print("É um panagrama" if checa_panagrama(frase2) else "Não é um panagrama")
