#start,end

start=int(input("Enter starting Number: "))
end=int(input("Enter end Number: "))
for num in range(start,end+1):
    is_Prime=True
    for i in range(2,num):
        if num%i==0:
            is_Prime=False
            break
        else:
            is_Prime=True
    if is_Prime==True:
        print(num)