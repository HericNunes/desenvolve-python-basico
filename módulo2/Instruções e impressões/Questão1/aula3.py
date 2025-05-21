salario_hora = 20
horas_por_semana = 40

salario_bruto = salario_hora * horas_por_semana
desconto_inss = 0.1 * salario_bruto
desconto_sind = 0.05 * salario_bruto
salario_liquido = salario_bruto - desconto_inss - desconto_sind

print("O salario bruto é", salario_bruto)
print("O desconto INSS é", desconto_inss)
print("O desconto Sindicato é", desconto_sind)
print("O salario liquido é", salario_liquido)
