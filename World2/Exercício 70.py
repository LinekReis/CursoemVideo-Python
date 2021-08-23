cheapestname = product = ''
amount = cheapest = value = higher1000= 0
higher1000 = 0
while True: 
   product = str(input("Type the name pf the product: "))
   value = int(input("Value of that product: "))
   cheapest = value
   amount += value 
   if value > 1000:
     higher1000 += 1
   if value < cheapest:
     cheapestname = product
   print("Press any button to continue\nOr type 'No' to end the program") 
   resp = str(input("Do you want to continue ? ")).upper()
   if resp == 'NO':
     break 
print(f"Quantity of products that costs\nmore or equal than U$ 1000 {higher1000}")
