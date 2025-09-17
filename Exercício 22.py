
numeros = []

while True:
    n = int(input("Insira um número: "))

    numeros.append(n)
    if n == 0:  # Verifica se a entrada é zero
        break
print(f"Total de elementos: {len(numeros)}")

somaPares = 0
somaImpares = 0
quantImpares = 0

for i in numeros:
    if i % 2 == 1:
        print('ímpar')
        somaImpares = somaImpares + i
        quantImpares = quantImpares + 1
    elif i % 2 == 0:
        print('par')
        somaPares = somaPares + i      
print(f'A soma dos números é {somaPares}')

mediaImpares = somaImpares / quantImpares
print(f'A média dos ímpares é {mediaImpares}')