counter=1
number=7
while counter<=5:
    print("Enter ", counter, " choice: ")
    x=int(input())
    if x==number:
        print("Good guess")
    else:
        print("Try again")
    counter+=1