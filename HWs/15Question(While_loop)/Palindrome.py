#5. Write a python program that checks if a given number is a palindrome using a 'while' loop

num=int(input("Enter a number: "))
temp=num
reversed_num=0
while(num>0):
    digit=num%10
    reversed_num=reversed_num*10 + digit
    num=num//10

if(temp==reversed_num):
    print(f"The number {reversed_num} is Palindrome")
else:
    print(f"{reversed_num} is not a palindrome")