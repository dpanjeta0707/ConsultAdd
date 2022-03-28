
print(" 1. Addition \n 2. Subtraction \n 3. Division \n 4. Multiplication \n 5. Average")

token=int(input("enter your choice: "))

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

if token==1:
    sum=num1+num2
    print("sum is ",sum )
    if sum<0:
        print("NEGATIVE")
elif token==2:
    diff=num1-num2
    print("difference is ",diff )
    if diff<0:
        print("NEGATIVE")
elif token==3:
    div=num1/num2
    print("fraction is ",div )
    if div<0:
        print("NEGATIVE")
elif token==4:
    product=num1*num2
    print("product is ",product )
    if product<0:
        print("NEGATIVE")
elif token==5:
    first=int(input("enter third number: "))
    second=int(input("enter fourth number: "))
    avg=(num1+num2+first+second)/4
    print("average is ",avg )
    if avg<0:
        print("NEGATIVE")
