#8. Greatest common Divisor (gcd) of two numbers using while loop.
num1 = float(input(" Please Enter the First Value : "))
num2 = float(input(" Please Enter the Second Value: "))

i = 1
while(i <= num1 and i <= num2):
    if(num1 % i == 0 and num2 % i == 0):
        val = i
    i = i + 1
    
print("\n HCF of {0} and {1} = {2}".format(num1, num2, val))