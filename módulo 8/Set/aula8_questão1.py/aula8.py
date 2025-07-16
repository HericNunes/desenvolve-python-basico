frase = "O rato roeu a roupa do Robson"
caracteres_unicos = set(frase.lower())
caracteres_sem_espaco = caracteres_unicos - {' '}
ordenados = sorted(caracteres_sem_espaco)
print("Caracteres únicos ordenados:", ordenados)
