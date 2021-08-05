print("Formação de Triângulo")
print("-"*26)
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 < lado3+lado2 and lado2 < lado1+lado3 and lado3 < lado1+lado2:
    print("Status: Possível Formar um triângulo")
    if lado1 == lado2 == lado3:
        print("Tipo de Triângulo: Equilatero ")
    elif lado1 != lado2 != lado3 != lado1:
        print("Tipoi de Triangulo: Isósceles")
    else:
        print("Tipo de Triângulo: Escaleno")
else:
    print("Status: Não é possível formar um triângulo")
