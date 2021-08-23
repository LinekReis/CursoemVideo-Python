cheapest = product = ''
amount = value = higher1000= 0
higher1000 = 0
while True: 
   product = str(input("Type the name pf the product: "))
   value = int(input("Value of that product: "))
   amount += value 
   if value > 1000:
     higher1000 += 1
   if value < cheapest:
     cheapest = product
   print("Press any button to continue\nOr type 'No' to end the program") 
   resp = str(input("Do you want to continue ? ")).upper()
   while resp != 'NO':
       print("Press any button to continue\nOr type 'No' to end the program") 
       resp = str(input("Do you want to continue ? ")).upper 
print(f"Quantity of products that costs\nmore or equal than 1000 {higher1000}")
