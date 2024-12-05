num=int(input("Enter a number: "))
total=0
for i in range(1,num):
    if num%i==0:
        total=total+i
print(total)
print("perfect" if total==num else "not perfect")