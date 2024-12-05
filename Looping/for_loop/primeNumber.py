# To print whether the number is prime or not

num=int(input("Enter number: "))

is_Prime=True

for i in range(2,num):
    if num%i==0:
        is_Prime=False
        break

print(is_Prime)