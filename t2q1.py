number=int(input("enter the number"))

if number%3==0 and number%5==0:
    print("“Consultadd - Python Training”")
elif number%3!=0 and number%5==0:
    print("Python Training")
elif number%3==0 and number%5!=0:
    print("Consultadd")
else:
    print("Lucky number")
