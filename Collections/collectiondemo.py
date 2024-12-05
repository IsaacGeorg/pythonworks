# COLLECTIONS

#When a groups is managed  Collection is used

# define is duplicates-allowed    insertion-order preserved            mutable


#    list=>          allowed               yes                             yes
#    set=>           Not allowed           

#Group of Numbers: List, Set, Tuple, Dictionary

text="hello"
text2='text2'
text3="""Hello There"""

expenses=[10000, 12000, 13000, 11000]
print(expenses[1])

colors=["Red", "Green", "Blue","Green","Blue"]
print(colors[1])
colors[0]="Pink"
print(colors)

color={"Red","Green","Blue","Green"}
print(color)


expenses=[10000, 12000, 13000, 11000]
expenses[0]=15000
print(expenses)

for exp in expenses:     # printing the collection of objects from one by one using for loop.
    print(exp)


#Calculating the total expenses in the list.
total=0
for exp in expenses:
    total=total+exp
print(total)

#Finding the max value without using max()
expenses=[10000, 12000, 13000, 11000]
max_exp=0
for exp in expenses:
    if exp>max_exp:
        max_exp=exp
print(max_exp)


#min
#avg
#most frequent expense

arr=[10,20,30,40]
for i in range(0,len(arr)):
    print(arr[i])


# Print the even elements in the list iterate using list
arr=[1,2,3,4,5,6,7,8,9,10,11]
for i in range(0,len(arr)):
    if arr[i]%2==0:
        print(arr[i])

arr=[2,3,4,5]
sum=8
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        twonum=arr[i]+arr[j]
    if twonum==sum:
        print((arr[i],arr[j]))


arr=[2,3,4,5]
sum=7
left=0
right=len(arr)-1
while (left<right):
    cur_sum=arr[left]+arr[right]
    if cur_sum==sum:
        print(arr[left],arr[right])
        left+=1
        right-=1
    elif cur_sum>sum:
        right-=1
    elif cur_sum<sum:
        left+=1


# lst=[2,3,4,5]
# sum=[]
# for i in range(0,len(lst)):
#     lst.remove(lst[i])
#     sum=sum+lst
#     print(lst)
