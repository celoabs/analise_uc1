idade = int(input("Digite a sua idade: "))

if idade < 5:
    print("Idade inválida.")
elif 5 <= idade <= 7:
    print("Infantil A")
elif 8 <= idade <= 10:
    print("Infantil B")
elif 11 <= idade <= 13:
    print("Juvenil A")
elif 14 <= idade <= 17:
    print("Juvenil B")
else: # Idade maior que 18
    print("Adulto")