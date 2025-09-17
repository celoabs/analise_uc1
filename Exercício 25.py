dono1 = {'nome' : 'marcelo', 'idade' : 48}

print(dono1['nome'])
print(dono1['idade'])

dono1['nome'] = 'Marcelo Augusto'
print(dono1['nome'])

dono1['celular'] = '99616-7281'
print(dono1['celular'])

dono1['animais'] = ['Olivia', 'Monica', 'Magali']
print(dono1['animais'])

dono2 = {'nome' : 'raquel', 'idade' : 45}
dono3 = {'nome' : 'rebeca', 'idade' : 26, 'animais' : ['joca','mingau']}

contatos = []
contatos.append(dono1)
contatos.append(dono2)
contatos.append(dono3)

for i in contatos:
    print(f"{i['nome']} - {i['idade']}")
    try:
        for j in i['animais']:
            print(j)
    except:
        print('Não possui animais')
 




