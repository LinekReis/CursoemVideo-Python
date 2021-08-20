print("Working with Numbers")
print("-"*20)

number = 0
total = 0
count = 0

while number != 999:
    number=int(input("Tipe a number: "))
    total += number
    count += 1 
    if number == 999:
        total -= 999
        count -= 1
print("Sum of the numbers: {}\nQuantity of numbers tiped: {}".format(total,count))
