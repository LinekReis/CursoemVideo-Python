print("Alistamento EB")
print("-"*14)

idade = int(input("Digite a sua idade:"))

if idade == 18:
    print("Ótimo voce está na idade correta de se alistar\npor favor procure a junta de serviço militar mais próxima")
elif idade > 18:
    print("Você passou {} da idade correta para se alistar ao serviço militar".format(idade-18))
    print("por favor procure a junta de serviço militar mais próxima\npara atualizar a sua situação com o serviço militar.")
else:
    print("Você ainda não chegou na idade de se alistar, ainda faltam {} anos".format(18-idade))
