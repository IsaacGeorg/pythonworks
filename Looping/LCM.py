#LCM of a number
m=int(input("Enter first number: "))
n=int(input("Enter second number: "))
i=1
while(i<=m and i<=n):
    if m%i==0 and n%i==0:
        gcd=i
    i=i+1
print(gcd)
lcm=(m*n)/gcd
print(lcm)