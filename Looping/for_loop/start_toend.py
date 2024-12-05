#Print all numbers from start to end
#read=start,end

start=int(input("Enter number: "))
end=int(input("Enter end number:"))

if start<end:
    for i in range(start,end+1,1):
        print(i)
else:
    for i in range(start,end-1,-1):
        print(i)