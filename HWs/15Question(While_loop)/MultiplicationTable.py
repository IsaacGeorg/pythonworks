#Q15. Write a python program to print the multiplication table of a given number using while loop.

n=int(input("Enter a number: "))
i=1
while i<=n:
    value=n*i
    print(f"{n} * {i} = {value}")
    i=i+1