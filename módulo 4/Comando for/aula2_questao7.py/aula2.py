produto = 1
tem_positivo = False  
while True:
    numero = int(input())
    
    if numero == 0:
        break
    
    if numero > 0:
        produto *= numero
        tem_positivo = True

if tem_positivo:
    print(f"Produto: {produto}")
else:
    print("Nenhum valor positivo foi digitado.")
