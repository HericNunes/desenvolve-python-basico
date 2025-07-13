import csv

mais_tocadas = {}

with open("spotify-2023.csv", encoding='latin-1') as arquivo:
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor)

    for linha in leitor:
        if len(linha) != 10:
            continue

        track_name = linha[0]
        artist_name = linha[1]
        try:
            artist_count = int(linha[2])
            released_year = int(linha[3])
            streams = int(linha[8])
        except ValueError:
            continue  
        if artist_count != 1:
            continue
        if 2012 <= released_year <= 2022:
            if released_year not in mais_tocadas or streams > mais_tocadas[released_year][3]:
                mais_tocadas[released_year] = [track_name, artist_name, released_year, streams]
resultado = [mais_tocadas[ano] for ano in sorted(mais_tocadas)]
print(resultado)
