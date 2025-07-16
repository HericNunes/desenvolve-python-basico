import string
from collections import Counter
caminho = "estomago.txt"
with open(caminho, "r", encoding="utf-8") as f:
    texto = f.read()
texto_limpo = texto.translate(str.maketrans('', '', string.punctuation)).lower()
palavras = texto_limpo.split()
frequencias = Counter(palavras)
frequencias_ordenadas = dict(sorted(frequencias.items(), key=lambda x: x[1], reverse=True))
for palavra, contagem in list(frequencias_ordenadas.items())[:20]:
    print(f"{palavra}: {contagem}")
