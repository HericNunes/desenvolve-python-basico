import re
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
palavras = re.findall(r'\b[a-zA-Zá-úÁ-ÚçÇ]+\b', conteudo)
with open("palavras.txt", "w", encoding="utf-8") as saida:
    for palavra in palavras:
        saida.write(palavra + "\n")
with open("palavras.txt", "r", encoding="utf-8") as resultado:
    print(resultado.read())
