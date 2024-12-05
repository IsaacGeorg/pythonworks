# armstrong number
# countdigit
# numbers within range
# reverse range
# lcm
# fibonacci 
# isfibonacci

#list methods: append(),pop(),insert(),index(),sort(),copy(),extend(),reverse(),count(),remove()

color=["red","yellow","green"]
color.append("blue")
print(color)
color.pop(1)
print(color)
color.reverse()
print(color)

# Create a list with the following elements: 1, 2, 3, 4, 5.
# Add the number 6 to the list.
# Remove the number 2 from the list.
# Print the reversed list.
# Output the final list and its length.

lst=[1,2,3,4,5]
lst.append(6)
lst.pop(1)
lst.reverse()
print(lst,len(lst))
lst[2]=10
print(lst)

# Given two lists: list1 = [1, 3, 5, 7] and list2 = [2, 3, 6, 7],
# Write a Python program to merge both lists, removing duplicates and maintaining order.
# Also, generate and print all possible 2-element combinations from list1.

list1=[1,3,5,7]
list2=[2,3,6,7]
list3=[]
for i in list1:
    if i not in list3:
        list3.append(i)
        for i in list2:
            if i not in list3:
                list3.append(i)

print(list3)

for i in range(0,len(list1)):
    for j in range(i+1,len(list1)+1):
        if list1[i]==list1[j]:
            break
        # else:
