print("-"*12)
print("Ano Bissexto")
print("-"*12)
ano = int(input("Digite um ano "))

if ano%4==0 and (ano%100!=0) or ano%400==0:
    print("O ano digitado equivale a um ano bissexto")
else: 
    print("O ano digitado não é um ano bissexto")