# 1. Find missing positive integer from [0,1,3,4,5]

arr1=[0,1,2,4,5]
arr=[]
for i in range(0,len(arr1)-1):
    if arr1[i]-arr1[i+1]!=-1:
        arr=arr1[i]+1
print(arr)

# 2. Find least postive integer from arr2=[1,2,3,4,5]

arr2=[1,2,3,4,5]
missing=[]
for i in range(1,len(arr2)+2):
    if i not in arr2:
        missing=i
        break

print(missing)