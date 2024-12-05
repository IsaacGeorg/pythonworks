arr=[1,2,2,2,1,4,5]
duplicate=[]
arr.sort()
for i in range(0,len(arr)-1):
    if arr[i]==arr[i+1]:
        if arr[i] not in duplicate:
            duplicate.append(arr[i])


print(duplicate)

print(dir(list))
lis1=[2,8,4,6,2]
lis2=[3,5,2,6,8]
lis1.extend(lis2)
lis1.remove(8)

print(lis1)