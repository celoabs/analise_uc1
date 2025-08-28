#exercício 6
AnoNascimento = int(
    input(f'Informe o ano de seu nascimento: '))
AnoAtual = int(
    input(f'Informe o ano atual: '))

idadeAnos = AnoAtual - AnoNascimento
idadeMeses = idadeAnos * 12
idadeDias = idadeAnos * 365
#IdadeDias = idadeMeses * 30

print(f'A sua idade em anos é {idadeAnos}')
print(f'A sua idade em meses é {idadeMeses}')
print(f'A sua idade em dias é {idadeDias}')


