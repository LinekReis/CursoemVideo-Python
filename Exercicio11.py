print("-"*18)
print(" Tinta Necessária ")
print("-"*18)
larg=float(input("Digite a largura da parede : "))
altu=float(input("Digite a altura da parede : "))
area=larg*altu
print("-"*18)
print("A parede tem uma área de {} m²\n1 litro pinta 2m²\nSerão necessários {}L de tinta\npara pintar a parede inteira".format(area,(area/2)))