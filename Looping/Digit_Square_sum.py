
num=int(input("Enter a number: "))
sum=0
while(num!=0):
    digit=num%10
    multiple=digit**2
    sum=sum+multiple
    num=num//10
print(sum)