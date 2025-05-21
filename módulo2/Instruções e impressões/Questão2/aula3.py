salario_hora = 20
horas_por_semana = 40

salario_bruto  = salario_hora * horas_por_semana
salario_liquido = salario_bruto - 0.1 * salario_bruto - 0.05 * salario_bruto

print ("O salario bruto é", salario_bruto)
print("O salario liquido é", salario_liquido)