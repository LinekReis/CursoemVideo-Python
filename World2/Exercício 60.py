//first option 
number = int(input("Tipe a value to calcule the factorial: "))
count = number

while count > 1:
    count -= 1
    number = number * count
    
print(number)
