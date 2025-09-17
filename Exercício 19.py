# Uma empresa almeja um programa que fará a leitura de 5 preços
# de produtos e no final irá exibir apenas o somatório dos produtos que 
# custam acima de 200 reais

soma = 0
for i in range(5):
    preco = float(input(f"Informe o preço: "))
    if soma >= 200:
        soma = soma + preco

print(f'O somatório dos produtos acima de R$ 200 é: {soma}')

