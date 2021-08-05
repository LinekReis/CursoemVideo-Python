print("Classificação de Atletas")
print("-"*31)
idade = int(input("Digite a idade do atleta: "))
if idade <= 9:
    print("Classificação do atleta: Mirim")
elif idade > 9 and idade <= 14:
    print("Classificação do atleta: Infantil")
elif idade > 14 and idade <= 19:
    print("Classificação do atleta: Júnior")
elif idade > 19 and idade <= 25:
    print("Classificação do atleta: Sênior")
else:
    print("Classificação do atleta: Master")
