string = input("enter your string")
 
digits = 0
letters = 0
 

for x in string:
 
    
    if x.isnumeric():
        digits += 1
 
    else:
        letters += 1
 
print("Total letters found : ", letters)
print("Total digits found : ", digits)