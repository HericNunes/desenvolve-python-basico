distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))
if distancia <= 100:
    preco_por_kg = 1.0
elif distancia <= 300:
    preco_por_kg = 1.5
else:
    preco_por_kg = 2.0
valor_frete = preco_por_kg * peso
if peso > 10:
    valor_frete += 10
print(f"Valor do frete: R${valor_frete:.2f}")
