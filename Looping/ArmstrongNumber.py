num=int(input("Enter a number: "))
original=num
length=len(str(num))
print(length)
sum=0
while(num!=0):
    digit=num%10
    multiple=digit**length
    sum=multiple+sum
    num=num//10
print(sum)
if sum==original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")