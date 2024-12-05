num=int(input("Enter the number: "))

# SYNTAX
# if condition:
#     stmt1
#     stmt2
#     stmt3

# else:
#     stmt4
#     stmt5
#     stmt6

if num>0:
    print(f"{num} is positive(+ve)")

else:
    print(f"{num} is negative(-ve)")


# Python program to print if eligible for voting or not

age=int(input("Enter your age: "))
if age>=18:
    print("Eligible for voting")

else:
    print("Not eligible for voting")