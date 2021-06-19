import random

numero = random.randint(0,5)
advinha = int(input("Digite o número que o computador pensou: "))

if advinha==numero:
 print("Parabéns número advinhado!")
else:
    print("O número que você digitou\nnão é o número que o computador pensou")