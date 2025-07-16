def encontra_diferenca(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)

    if len(lista1) > len(lista2):
        diferenca = set1 - set2
        origem = "segunda"
    else:
        diferenca = set2 - set1
        origem = "primeira"
    
    if diferenca:
        elemento = diferenca.pop()
        print(f"O elemento {elemento} está faltando na {origem} lista.")
    else:
        print("As listas são idênticas.")
A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]
encontra_diferenca(A, B)
