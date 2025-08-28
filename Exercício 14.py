# uma empresa precisa que qdo o usuário digitar o número 1, o programa imprimirá a palavra 'Alimentos'
# se o usuário digitar o número 2, imprimirá a palavra 'Bebidas'
# se o usuário digitar o número 3 ou 4, imprimirá a palavra 'Cosméticos'
# se o usuário digitar o número 5 ou 6, imprimirá a palavra 'Produtos de Limpeza'
# qualquer outro, o programa imprimirá 'Categoria não encontrada'

numero = int(input("Digite um número de 1 a 6: "))

if numero == 1:
    print("Alimentos")
elif numero == 2:
    print("Bebidas")
elif numero == 3 or numero == 4:
    print("Cosméticos")
elif numero == 5 or numero == 6:
    print("Produtos de Limpeza")
else:
    print("Categoria não encontrada")