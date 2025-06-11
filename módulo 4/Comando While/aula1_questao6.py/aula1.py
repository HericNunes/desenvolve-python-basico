n = int(input("Digite o número de experimentos: "))

total = 0
sapos = 0
ratos = 0
coelhos = 0

for _ in range(n):
    entrada = input("Digite a quantidade e o tipo (C, R, S): ").split()
    quantia = int(entrada[0])
    tipo = entrada[1].upper()  

    total += quantia

    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

perc_coelhos = (coelhos / total) * 100 if total else 0
perc_ratos = (ratos / total) * 100 if total else 0
perc_sapos = (sapos / total) * 100 if total else 0

print(f"\nTotal de cobaias: {total}")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f} %")
print(f"Percentual de ratos: {perc_ratos:.2f} %")
print(f"Percentual de sapos: {perc_sapos:.2f} %")
