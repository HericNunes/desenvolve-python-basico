nome1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o preço unitário do produto 1:"))
quant1 = int(input("Digite a quantidade do produto 1:"))

nome2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o preço unitário do produto 2:"))
quant2 = int(input("Digite a quantidade do produto 2:"))

nome3 = input("Digite o nome do produto 3:")
preco3 = float(input("Digite o preço unitário do produto 3:"))
quant3 = int(input("Digite a quantidade do produto 3:"))

total = (preco1 * quant1) + (preco2 * quant2) + (preco3 * quant3)
print(f"Total: R${total:,.2f}")