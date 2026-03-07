num=int(input("Enter a lucky number from (1-10):"))
while True:
    num1=int(input("Enter a your number from (1-10):"))
    if num1<10:
        if num==num1:
            print("Winner")
            break
        else:
            if num>num1:
                print("Too low")
            else:
                print("Too high")
    else:
        print("Number greater than 10")
        print()