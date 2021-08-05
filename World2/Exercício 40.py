print("Média Aritmética")
print("-"*16)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2

if media < 5:
    print("Infelizmente você foi reprovado")
    print("Sua média foi de: {} pontos".format(media))

elif media >= 5 and media < 7:
    print("Infelizmente você ficou de recuperação\nmas ainda há chances de você passar")
    print("Sua média foi de: {} pontos".format(media))

elif media >= 7:
    print("Parabéns você foi aprovado!")
    print("Sua média foi de {}".format(media))
