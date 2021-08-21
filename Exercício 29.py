velocidade = float(
    input("Qual foi a velocidade que o carro passou no radar ? "))

if velocidade <= 80:
    print("O carro estava dentro do limite da via nenhuma multa será aplicada!")
else:
    print("Carro multado o carro excedeu o limite permitido na via!")
    print("Velocidade limite: 80\nVelocidade registrada pelo radar: {}".format(velocidade))
    multa = (velocidade-80)*7
    print("Multa a pagar: R$ {:.2f} !".format(multa))
