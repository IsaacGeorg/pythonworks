#7. Write a python program to count the number of digits in a given number using a 'while' loop

number=int(input("Enter the number: "))
count=0
while(number>0):
    count=count+1
    number=number//10

print(count)
