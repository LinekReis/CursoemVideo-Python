amount = cheap = higher1000 = 0
cheapname = ''
while True: 
    product = str(input("Type the name of the product: "))
    value = float(input("Value of that product: "))
    amount += value 
    if value > 1000:
     	higher1000 += 1
    if value < cheap:
	cheap = value
	cheapname = product
    print("Press any button to continue\nOr type 'No' to end the program") 
    resp = str(input("Do you want to continue ? ")).upper()
    if resp == 'NO':
        break 
print(f"Quantity of products that costs\nmore or equal than U$ 1000 {higher1000}")
print(f"The total value of the shop: U$ {amount}")
print(f"And the name of the cheapest one is: {cheapname}")
