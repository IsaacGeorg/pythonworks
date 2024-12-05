#Q1. Read 2 numbers, print the largest number

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if num1>num2:
    print(f"{num1} is the largest number when compared to {num2}")
else:
    print(f"{num2} is the largest number when compared to {num1}")



#Q2. Read 3 numbers num1, num2, num3 and print the largest among the three numbers

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if num1>num2 and num1>num3:
        print(num1)
elif num2>num1 and num2>num3:
        print(num2)
    
elif num3>num2 and num3>num1:
    print(num1)
elif num1==num2 and num1==num3 and num2==num3:
    print("Three numbers are equal")


#Q3. Read 3 numbers num1, num2, num3 and print the second largest among the three numbers

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if num1>num2 and num1>num3:
    if num2>num3:
        print(f"The second largest number: {num2}")
    else:
        print(f"The second largest number: {num3}")

elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"The second largest number: {num1}")
    else:
        print(f"The second largest number: {num3}")

elif num3>num2 and num3>num1:
    if num1>num2:
        print(f"The second largest number: {num2}")
    else:
        print(f"The second largest number: {num1}")



#Q4. Read 3 numbers num1, num2, num3 and sort these 3 numbers without using function

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if num1>num2 and num1>num3:
    if num2>num3:
        print(num1,">",num2,"<",num3)
    else:
        print(num1,"<",num3,"<",num2)
elif num2>num1 and num2>num3:
    if num1>num3:
        print(num2,"<",num1,"<",num3)
    else:
        print(num2,"<",num3,"<",num1)
elif num3>num2 and num1<num3:
    if num2>num1:
        print(num3,"<",num2,"<",num1)
    else:
        print(num3,"<",num1,"<",num2)