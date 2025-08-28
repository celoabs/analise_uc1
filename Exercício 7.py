"""exercício 7 Faça um programa que fará a leitura de uma temperatura em graus Kelvin e apresentá-la em graus Celsius"""

kelvin = float(
    input(f'Informe a temperatura em Kelvin: '))
    
celsius = kelvin - 273.15

print(f'A temperatura em graus Celsius é {celsius:.2f}')


"""exercício 8 Escreva um programa que converta uma temperatura digitada em °C em °F"""
C = float(
    input("Digite a temperatura em °C:"))

F = (9 * C / 5) + 32

print("%5.2f°C é igual a %5.2f°F" % (C, F))