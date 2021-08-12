print("-"*26)
print("Highest and lowest weights")
print("-"*26)

highest = 0
lowest = 0

for i in range (0,5):
    weight = int(input("Tipe the weight: "))
    if i == 1:  
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        if weight < lowest:
            lowest = weight
        
print("The highest was {}kg, and the lowest was {}kg ".format(highest,lowest))
