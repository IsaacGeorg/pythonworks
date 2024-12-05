
# Print the max of two numbers
def max_two(num1,num2):
    return max(num1,num2)
    
print(max_two(12,4))

# Print the min of two numbers
def min_two(num1,num2):
    return min(num1,num2)
    
print(min_two(12,4))


#multiplication table
def multiplication_table(num,n=10):
    for i in range(1,n+1):
        result=num*i
        print(f"3*{i}={result}")  

multiplication_table(3)

#Exponent of a number
def exponent(num,n):
    return num**n
print(exponent(4,3))

# Print the return value if the return==True or False
def smart_sub(num1,num2,reverse):
    return num2-num1 if reverse==True else num1-num2
    
print(smart_sub(18,3,True))
print(smart_sub(18,3,False))


# To print numbers from 1 to 10
def random_numbers(start,end,step=1):
    while(start<=end):
        print(start,end="\t")
        start=start+step
    return
start=int(input("Start:"))
end=int(input("End: "))
random_numbers(start,end)


import random
print(random.randint(10,20))


# is_perfect_number(number)
# is_armstrong_number(number)
# is_palindrome_number(number)