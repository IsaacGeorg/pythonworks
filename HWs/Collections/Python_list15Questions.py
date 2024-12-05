# 1. Write a python program to find the sum of all elements in a list.

lst=[22,4,36,72,18]
sum=0
for i in range(0,len(lst)):
    sum+=lst[i]
print(f"Answer for Q1: The Sum of the list {lst} is {sum}\n")


# 2. Write a python program to remove duplicates from a list.

lst=[2,4,3,6,2,5,3,6,3]
lst.sort()
removedupe=[]
for i in lst:
    if i not in removedupe:
        removedupe.append(i)

print(f"Answer for Q2:",removedupe,"\n")


# 4. Write a python program to count the occurence of each element in the list.
print("Answer for Q4:")
lst=[2,4,2,4,5,2,33,32,5,3,2]
lst.sort()
count=1
for i in range(1,len(lst)):
    j=i-1
    if lst[i]==lst[j]:
        count+=1
    else:
        print(lst[j],"occurs",count, "times\n")
        count=1
print(lst[-1],"occurs",count, "times\n")


# 5. Write a python program to reverse a list.
print("Answer for Q5:")
lst=[21,22,23,24,25,26,27]
print(lst[::-1],"\n")

# 6. Write a python program to find the maximum and minimum elements in a list.
print("Answer for Q6:")
lst=[21,34,25,14,75,44]
lst.sort()
print(f"Maximum_number:{max(lst)},Minimum_Number: {min(lst)}\n")

#7. Write a python program to merge two lists and sort the resulting list.
print("Answer for Q7:")
lst1=[23,1,45,12,5,28,34]
lst2=[3,6,24,16,54,36]
lst1.extend(lst2)
lst1.sort()
print(f"ExtendedList:{lst1} \n")

# 8. Write a python program to find common elements in two lists.
print("Answer for Q8:")
lst1=[3,4,65,23,56,36,8]
lst2=[5,56,23,6,8]
lst1.sort()
lst2.sort()
i=0
j=0
while(i<len(lst1)and j<len(lst2)):
    if lst1[i]==lst2[j]:
        print(f"{lst1[i]}\n")
        i+=1
        j+=1
    elif lst1[i]<lst2[j]:
        i+=1
    elif lst1[i]>lst2[j]:
        j+=1

# 9. Write a python program to check if a list is empty
print("Answer for Q9:")
lst=[23]
is_empty=False
if lst==[]:
    is_empty=True
    print(is_empty,"\n")
else:
    print(is_empty,"\n")

# 10. Write a python program to remove an element from a list by index.
print("Answer for Q10:")
lst=[3,4,65,23,56,36,8]
ind=lst.pop(3)
print(f"Removed Element:{ind}\n")

# 11. Write a python program to find the length of a list without using the len() function.
print("Answer for Q11:")
lst=[2,4,1,6,3,8]
length=0
for i in lst:
    length+=1
print(f"Length of the List:{length}\n")

# 12. Write a python program to multiply all the elements in a list.
print("Answer for Q12:")
lst=[2,4,1,6,3,8]
multiply=1
for i in lst:
    multiply=multiply*i
print(multiply,"\n")

# 13. Write a python program to find all the even numbers in a list.
print("Answer for Q13:")
lst=[2,4,1,6,3,8]
for point in lst:
    if point%2==0:
        print(f"{point} is an even number.\n")

# 14. Write a python program to replace an element in a list with another element.
print("Answer for Q14:")
lst=[2,4,1,6,3,8]
lst.pop(2)
lst.insert(2,10)
print(f"After element replacement in List:{lst}\n")

# 15. Write a python program to split a list into two halves.
print("Answer for Q15:")
lst=[2,4,1,6,3,8]
mid=len(lst)//2
first_half=lst[:mid]
second_half=lst[mid:]
print(f"First_Half:{first_half}")
print(f"Secold half:{second_half}")
