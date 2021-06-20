print("-"*21)
print("Formação de Triângulo")
print("-"*21)

lado1=float(input("Digite o primeiro lado: "))
lado2=float(input("Digite o segundo lado: "))
lado3=float(input("Digite o terceiro lado: "))

if lado1<lado2+lado3 and lado2<lado1+lado3 and lado3<lado1+lado2:
    print("De acordo com os 3 números digitados\né possível formar um triângulo!")
else:
    print("Com base nos três números digitados\nnão é possível formar um triângulo!")