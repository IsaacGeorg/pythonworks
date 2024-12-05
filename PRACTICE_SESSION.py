def number(n): #4th place must be printed
    a=3
    b=4
    print(a)
    print(b)
    for i in range(2,n):
        add=a+b
        print(add)
        a=b
        b=add
    return 

number(4)
# print(result)

# *
# **
# ***
# ****

for rows in range(7,1):
    for cols in range(1,rows+1):
        print("*",end="\t")
    print()