#Altura em metros e o sexo de uma pessoa (M masculino e F feminino) calcule o peso ideal
# para homens (72.7*h) - 58
# para mulheres (62.1*h) - 44.7


h = float(
    input(f'Informe sua altura em metros: '))
sexo = (input('Digite M para masculino ou F para feminino: '))
pesoIdeal = 0.0

if sexo == "M" or sexo == "m":
    pesoIdeal = (72.7 * h) - 58
    
else:
    pesoIdeal = (62.1 * h) - 44.7
print(f"O peso ideal é: {pesoIdeal:.3f} kilos")
    

