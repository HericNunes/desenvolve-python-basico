fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)
celsius_int = int(celsius)
print(f"{fahrenheit} graus Fahrenheit são {celsius_int} graus Celsius.")