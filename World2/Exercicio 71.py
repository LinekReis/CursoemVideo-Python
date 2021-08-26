from time import sleep
from random import randint 
from system import os
nota20= 20
nota50 = 50
nota100 = 100
amount = 0
ncont = ''
while True:
    Print("Realizar Saque[1]\nRealizar débito [2]\nPagar Conta [3]")
   option = int(input("Digite a opção desejada: ")
     if option == 1:
        print("Notas disponíveis: R$ 20,R$ 50 e R$ 100")
        withdraw = int(input("Quanto deseja retirar ?")
       nota = int(input("Deseja retirar em nota de quanto ? ")
       if nota = 20:
         while nota20 < withdraw:
           count += 1
           nota20 += 20
       elif nota = 50:
         while nota50 < withdraw:
           c+= 1
           nota50 += 50
       elif nota = 100:
         while nota100 < withdraw: 
         c += 1
         nota100 += 100
      elif option = 2: 
        dep = int(input("Quanto deseja depositar ? "))
        amount += dep
      elif option = 3:
        ncont = str(input("Digite o código de barras: "))
   os.system('cls' if os.name == "nt" else 'clear')
         
       
