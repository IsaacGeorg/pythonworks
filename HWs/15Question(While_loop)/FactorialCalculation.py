#3. Write a python program to calculate the factorial of a given number using a 'while' loop

num=int(input("Enter factorial number: "))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i=i+1

print(f"The factoial of {num} is {fact}")