def ordenar_tuplas(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)
alunos_notas = [('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.0), ('David', 8.8)]
resultado = ordenar_tuplas(alunos_notas)
print(resultado)
