import numbers


lucky_number = 6
answer="yes"
while answer=="yes":
    number=int(input("Guess the number: "))
    if number==lucky_number:
        print("Congratulations! you guessed the right number")
        break
    answer=input("Do you want to continue? yes/no: ")

print("Thanks for playing.")