def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

num=int(input("Enter a number to get its Factorial: "))
result=factorial(num)
print(result)
