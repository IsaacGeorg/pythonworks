

# arr1=[10,2,8,13,20,4]
# arr2=[8,5,13,4]
# count=0

# for i in range(0,len(arr1)):
#     for j in range(0,len(arr2)):
#         if arr1[i]==arr2[j]:
#             print(arr1[i])
          
        
arr1=[10,4,5,7,8]
arr2=[3,6,2,8,4]
arr1.sort()
arr2.sort()
print(arr1)
print(arr2)

p1=0
p2=0

while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(arr1[p1])
        p1+=1
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1