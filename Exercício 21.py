#  a Martins Informática comercializa os seguintes produtos
# faça um programa que fará a leitura do código e a quantidade, 
# a cada iteração, o programa deverá perguntar se o usuário deseja continuar cadastrando itens.
# caso a resposta for 'n', o programa exibirá a soma e encerrará

soma = 0

while True:

    cod = int(input('Informe o código: '))
    qtt = int(input('Informe a quantidade: '))

    match (cod):
        case 10:
            soma = soma + (40*qtt)
        case 11:
            soma = soma + (130*qtt)
        case 12:
            soma = soma + (80*qtt)
        case 13:
            soma = soma + (15*qtt)
        case 14:
            soma = soma + (20*qtt)
        
        case _:
            print('Código inválido')

    r = input("Deseja continuar? (s/n) ")
    if r == 'n' or r=='N':
        break

print(f'O valor total é {soma:.2f}')



