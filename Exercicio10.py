print("-"*10)
print("USD to BRL")
print("-"*10)
usd=float(input("Qual o valor do do dólar atualmente ? "))
brl=float(input("Certo, deseja converter quantos R$ ? "))
convertido=brl/usd
print("-"*10)
print("R$ {} convertido para dólar é igual a {:.2f} USD".format(brl,convertido))