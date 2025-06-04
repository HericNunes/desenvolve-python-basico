valor_total = float(input("Digite o valor total da compra: "))
if valor_total >= 100:
    desconto_percentual = 20.0
elif valor_total >= 50:
    desconto_percentual = 10.0
else:
    desconto_percentual = 0.0
valor_final = valor_total * (1 - desconto_percentual / 100)
print(f"Desconto aplicado: {desconto_percentual}%")
print(f"Valor final com desconto: R${valor_final:.2f}")
