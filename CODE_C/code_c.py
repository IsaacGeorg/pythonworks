# Q1. Write a python program that reads an integer from the user and performs the following checks:

num=int(input("Enter a number: "))
if num%15==0:
    print("PINGPONG")
elif num%3==0:
    print("PING")
elif num%5==0:
    print("PONG")
else:
    print(num)



# Q2. Python program is the number is prime or not and if it is not, print the next prime number
num=int(input("Enter number: "))
is_Prime=True
next=1
for i in range(2,num):
    if num%i==0:
        is_Prime=False
        if is_Prime==False:
            num=num+next
print(is_Prime)
print(num)
