def valida_cpf(cpf_str):
    cpf_numeros = [int(c) for c in cpf_str if c.isdigit()]
    
    if len(cpf_numeros) != 11:
        return "Inválido"
    nove_digitos = cpf_numeros[:9]
    soma = sum([nove_digitos[i] * (10 - i) for i in range(9)])
    resto = soma % 11
    if resto < 2:
        dig1 = 0
    else:
        dig1 = 11 - resto
    dez_digitos = nove_digitos + [dig1]
    soma = sum([dez_digitos[i] * (11 - i) for i in range(10)])
    resto = soma % 11
    if resto < 2:
        dig2 = 0
    else:
        dig2 = 11 - resto
    if dig1 == cpf_numeros[9] and dig2 == cpf_numeros[10]:
        return "Válido"
    else:
        return "Inválido"
cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
print(valida_cpf(cpf))
