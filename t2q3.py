a=10
b=20
c=30
avg=(a+b+c)/3
print("average:", avg)

if avg>a and avg>b and avg>c:
    print("average is higher than a, b and c")
elif avg>a and avg>b and avg<=c:
    print("average is higher than a and b but not c")
elif avg>a and avg<=b and avg>c:
    print("average is higher than a and c but not b")
elif avg<=a and avg>b and avg<=c:
    print("average is higher than b and c but not a")
elif avg>a and avg<=b and avg<=c:
    print("average is higher than a but not b and c")
elif avg<=a and avg>b and avg<=c:
    print("average is higher than b but not a and c")
else:
    print("average is higher than c but not a and b")


