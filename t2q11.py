counter=1
number=7
while counter<=5:
    print("Enter ", counter, " choice: ")
    x=int(input())
    if x==number:
        print("Good guess")
        break
    else:
        print("Try again")
    if counter==5:
        print("Sorry but that was not very successful")
    counter+=1