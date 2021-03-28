from math import sqrt
catopos = float(input("Digite o cateto oposto de um triângulo retangulo: "))
catadja = float(input("Digite agora o cateto adjacente: "))
hipo = sqrt((catopos**2)+(catadja**2))
print("A hipotenusa desse triângulo é equivalente a : {:.2f}".format(hipo))
