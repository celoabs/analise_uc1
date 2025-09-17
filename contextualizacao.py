#lista
nome = 'Marcelo'
print(nome)
print(type(nome))
print(nome.upper())
print(f'A quantidade de letras de {nome} é {len(nome)}')


contatos = []
contatos.append('Marcelo')
contatos.append('Augusto')
print(contatos)
print(len(contatos))

frutas = ['pêra', 'uva', 'morango']
frutas = frutas + ['abacaxi', 'laranja']
print(frutas)
print(type(frutas))

frutas [4]= 'goiaba'
print(frutas)
print(len(frutas))

for f in frutas:
    print(f)

# eliminando elementos
frutas.pop(2) # por posição
print(frutas)
frutas.remove('uva') # pelo nome do objeto
print(frutas)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

