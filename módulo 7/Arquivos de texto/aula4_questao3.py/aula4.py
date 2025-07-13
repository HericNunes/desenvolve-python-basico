import re
with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
print("=== Primeiras 25 linhas ===")
for linha in linhas[:25]:
    print(linha.strip())
print("\n")
num_linhas = len(linhas)
print(f"Total de linhas: {num_linhas}")
linha_maior = max(linhas, key=lambda l: len(l))
print("\n=== Linha com mais caracteres ===")
print(linha_maior.strip())
print(f"Comprimento: {len(linha_maior)} caracteres")
texto_completo = ''.join(linhas)
nonato_count = len(re.findall(r'\bnonato\b', texto_completo, re.IGNORECASE))
iria_count = len(re.findall(r'\bíria\b', texto_completo, re.IGNORECASE))

print(f"\nMenções a 'Nonato': {nonato_count}")
print(f"Menções a 'Íria': {iria_count}")
