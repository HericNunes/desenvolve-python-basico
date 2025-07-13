def validador_senha(senha):
    if len(senha) < 8:
        return False
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    especiais = "@#$%&*?!"
    
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in especiais:
            tem_especial = True
    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return True
    else:
        return False
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  
print(validador_senha(senha2))  
print(validador_senha(senha3))  