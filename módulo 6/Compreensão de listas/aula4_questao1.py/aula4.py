pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]
print("Pares entre 20 e 50:", pares_20_50)

quadrados = [x**2 for x in [1,2,3,4,5,6,7,8,9]]
print("Quadrados:", quadrados)

div7 = [x for x in range(1, 101) if x % 7 == 0]
print("Divisíveis por 7 de 1 a 100:", div7)

par_ou_impar = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]
print("Paridade de range(0,30,3):", par_ou_impar)
