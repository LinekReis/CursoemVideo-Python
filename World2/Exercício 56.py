agesum = 0
womancount = 0
for i in range(0, 4):

    name = str(input("Tipe the name of the person: "))
    age = int(input("Tipe the age of the person: "))

    oldestage = age

    agesum += age

    if age > oldestage:
        oldestage = age

    print("Sex Selection")
    print("[1] Man\n[2] Woman\n")
    select = int(input("Choose the person sex: "))

    while select != 1 and select != 2:
        select = int(input("Choose the person sex: "))

    if age >= oldestage and select == 1:
        oldestname = name

    if select == 2 and age < 20:
        womancount += 1
print("The name of the oldest man is: {}\nAnd was registered {} girls younger than 20".format(
    oldestname, womancount))
