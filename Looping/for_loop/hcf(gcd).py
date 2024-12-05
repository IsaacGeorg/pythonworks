num1=int(input("Enter number: "))
num2=int(input("Enter number: "))

for i in range(1,num1+1,1):
    if num1%i==0 and num2%i==0:
        print(i)

