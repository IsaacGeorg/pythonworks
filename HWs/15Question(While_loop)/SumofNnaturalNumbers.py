# Python program to calculate Sum of first N natural numbers using a 'while loop'

N=int(input("Enter the limit of number to be SUM up: "))
sum=0
i=0
while(i<=N):
    sum=sum+i
    i=i+1
print(sum)