import string
while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if frase.lower() == "fim":
        break
    frase_limpa = frase.translate(str.maketrans('', '', string.punctuation))
    frase_limpa = frase_limpa.replace(" ", "").lower()
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo\n')
    else:
        print(f'"{frase}" não é palíndromo\n')
