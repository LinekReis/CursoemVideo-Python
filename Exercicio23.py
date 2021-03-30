print("-"*27)
num = int(input("Digite um valor de 0 a 9999: "))
print("-"*27)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("O numero digitado tem: ")
print("Milhares: {} ".format(m))
print("Centenhas: {} ".format(c))
print("Dezenas: {} ".format(d))
print("Unidades: {} ".format(u))
print("-"*27)
