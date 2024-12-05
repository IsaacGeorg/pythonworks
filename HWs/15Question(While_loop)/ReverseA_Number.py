# 4. Write a python program to reverse a given number using a 'while' loop

num=int(input("Enter random number: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num//10

print("Reversed Number: " + str(reversed_num))