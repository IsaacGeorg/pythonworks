# Q10. Write a python program to find the sum of digits of a given number using a 'while' loop.

num=int(input("Enter a number: "))
sum=0
rem=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10

print(sum)