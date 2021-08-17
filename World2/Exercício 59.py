firstnumber = int(input("Tipe the first number: "))
second = int(input("Tipe the second number: "))

option = 0

while option != 5:
    print("[1] Sum the two values\n[2] Multiply")
    print("[3] Greatest\n[4] New values\n[5] Exit program")
    option = int(input("Tipe the disered option: "))
    if option == 4:
        firstnumber = int(input("Tipe the first number: "))
        second = int(input("Tipe the second number: "))
