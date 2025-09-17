# Faça um programa que executará a conversão de temperaturas Celsius
# para Fahrenheit começando em 10 graus Celsius até 60°C, saltando de 5 em 5 graus
# A fórmula de conversão é F = 9C / 5 + 32

for C in range(10,61,5):
    F = 9 * C / 5 + 32
   
print(f"{C}°C equivale a {F}F")


