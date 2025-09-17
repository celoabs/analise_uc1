contatos = []

nome = 'marcelo'
nome = 'augusto'
print(nome)

contatos.append (nome)
contatos.append('santos')
print(contatos)

contatos.insert(0, 'raquel')
print(contatos)

print(contatos[1])
contatos[1] = 'rebeca'

for i in contatos:
    print(i)

contatos.append(20)
contatos.append(4.5)
print(contatos)

contatos.append(['araujo', 48])
print(contatos)
