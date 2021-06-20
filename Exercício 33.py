print("-"*18)
print("Menor e Maior Valor")
print("-"*18)
numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))
numero3 = int(input("Digite o terceiro valor: "))

if numero1>numero2 and numero2>numero3:
    maior = numero1
elif numero2>numero1 and numero2>numero3:
    maior = numero2
elif numero3 > numero2 and numero3>numero1:
    maior = numero3

if numero1<numero2 and numero1 < numero3:
    menor = numero1
elif numero2<numero1 and numero2<numero3:
    menor = numero2
elif numero3<numero1 and numero3 < numero2:
    menor = numero3

print("O maior valor foi: {}\nE o menor foi: {} ".format(maior,menor))