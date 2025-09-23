
from menu import *
cliente=[]
while True:
    menu()
    opcao = int(input('Digite opção:'))
    match opcao:
        case 1:
            cadastrar(cliente)
        case 2:
            listar(cliente)
        case 0:
            break
        case _:
            print("Opção Inválida")


