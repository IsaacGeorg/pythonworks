# Q6. Write a python program to print the fibonacci series up to a specified number using a 'while' loop.

num=int(input("Enter the limit: "))
a=0
b=1
c=0
i=0
print(a)
print(b)
while(i<=num):
    c=a+b
    a=b
    b=c
    print(c)
    i=i+1
   

