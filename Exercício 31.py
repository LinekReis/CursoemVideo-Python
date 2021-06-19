print("-"*14)
print("Cálculo de KM's")
print("-"*14)

kmrodado = int(input("Digite quantos KM's você rodou: "))

if kmrodado<=200:
    preco = kmrodado*0.50
    print("Preço a ser pago equivalente\na quantidade de KM's rodados: R$ {}".format(preco))
else:
    preco = kmrodado*0.45
    print("Preço a ser pago equivalente\na quantidade de KM's rodados: R$ {}".format(preco))