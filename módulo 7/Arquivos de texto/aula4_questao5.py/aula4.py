livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["Sapiens", "Yuval Noah Harari", 2011, 464],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 320],
    ["Capitães da Areia", "Jorge Amado", 1937, 256]
]
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        arquivo.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso.")
