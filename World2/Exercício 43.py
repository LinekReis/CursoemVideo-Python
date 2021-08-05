print("Índice de Massa Corporal")
print("-"*24)
altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em kg: "))
imc = (peso/(altura*altura))
print("-"*13)
print("Classificação")
print("-"*13)

if imc < 18.5:
    print("Abaixo do Peso")
    print("IMC: {}".format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print("Peso Normal")
    print("IMC: {}".format(imc))
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
    print("IMC: {}".format(imc))
elif imc >= 30 and imc <= 34.9:
    print("Obesidade Grau I")
    print("IMC: {}".format(imc))
elif imc >= 35 and imc <= 39.9:
    print("Obesidade Grau II")
    print("IMC: {}".format(imc))
else:
    print("Obesidade Grau III ou Mórbida")
    print("IMC: {}".format(imc))
