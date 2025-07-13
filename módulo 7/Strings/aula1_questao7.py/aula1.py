import random
def encrypt(lista):
    n = random.randint(1,10)
    nomes_cript = []
    for nome in lista:
        criptografado = ""
        for c in nome:
            codigo = ord(c)
            codigo_novo = codigo + n
            if codigo_novo > 126:
                codigo_novo = 33 + (codigo_novo - 127)
            criptografado += chr(codigo_novo)
        nomes_cript.append(criptografado)
    return nomes_cript, n
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nomes_cript, chave = encrypt(nomes)
print("Chave de criptografia:", chave)
print("Nomes criptografados:", nomes_cript)
