# uma escola solicita um programa que calcule e informe a média e a situação dos alunos
# para isso o programa deverá solicitar que o usuário informe as 4 notas
# se a média for maior ou igual a 7, deverá informar que o aluno está aprovado, senão, deverá pedir a nota de recuperação
# o programa fará um novo cálculo entre a média e a nota de recuperação, caso, essa nova média seja inferior a 5,
# o programa informará que o aluno está reprovado, senão, aprovado

nota1 = float(
    input("Informe a nota 1: "))
nota2 = float(
    input("Informe a nota 2: "))
nota3 = float(
    input("Informe a nota 3: "))
nota4 = float(
    input("Informe a nota 4: "))
notaRec = float(
    input("Informe a nota de recuperação: "))

somaTotal = nota1 + nota2 + nota3 + nota4
media = somaTotal / 4

print(f'A sua nota média é {media:.2f}')

if media >= 7:
    print("Você está Aprovado")
else: # pedir nota de recuperação
    print("Você está de Recuperação")

if notaRec < 5:
    print("Reprovado")
else:
    print("Aprovado")
