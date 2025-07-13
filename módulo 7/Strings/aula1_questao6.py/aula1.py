frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
objetivo_sorted = sorted(palavra_objetivo.lower())

palavras = frase.split()
anagramas = []

for palavra in palavras:
    palavra_limpa = palavra.strip(".,!?").lower()
    if sorted(palavra_limpa) == objetivo_sorted:
        anagramas.append(palavra)
print(f"Anagramas: {anagramas}")
