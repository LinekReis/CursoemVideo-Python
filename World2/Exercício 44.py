print("Método de Pagamento e Desconto")
print("-"*30)
preco = float(input("Informe o valor do produto: R$ "))
print("-"*19)
print("Método de pagamento")
print("-"*19)
print("[1] À vista dinheiro\n[2] Cheque\n[3] À vista no cartão")
print("[4] Parcelar até 2x no cartão\n[5] Parcelar 3x ou mais no cartão")
opcao = int(input("Digite a opção desejada: "))
if opcao == 1 or opcao == 2:
    preco = preco - (preco*0.1)
    print("Valor a pagar: R$ {}".format(preco))
elif opcao == 3:
    preco = preco - (preco*0.05)
    print("Valor a pagar: R$ {}".format(preco))
elif opcao == 4:
    print("Valor a pagar: R$ {}".format(preco))
elif opcao == 5:
    parcelas = int(input("Em quantas vezes deseja parcelar: "))
    valorparcelado = preco/parcelas
    novovalor = valorparcelado + (preco*0.20)
    print("Valor das parcelas: R$ {}".format(novovalor))
    print("Valor final do produto: R$ {}".format(novovalor*parcelas))
