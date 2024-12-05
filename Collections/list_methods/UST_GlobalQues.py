arr=[100,200,300,400,500,600,700,800]
oddelements=[]
for i in arr:
    if i%200!=0:
        oddelements=oddelements+[i]
print(oddelements)

odd_position_numbers=[num for index,num in enumerate(arr) if index%2!=0]
odd_position_numbers.reverse()
print(odd_position_numbers)

# for index,num in enumerate(odd_position_numbers):
#     arr[index+1]=num
# print(arr)

left=1
right=len(arr)-1
if right%2==0:
    right-=1

while(left<right):

    arr[left],arr[right]=arr[right],arr[left]
    left+=2
    right-=2

print(arr)

# for j in range(1,len(arr),2):
#     arr=oddposelements[i]
#     print(arr)