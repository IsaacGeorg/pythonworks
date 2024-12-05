
# LINEAR SEARCH

arr=[2,4,6,3,8,7]
search_element=int(input("Search number: "))
is_present=False
for i in range(0,len(arr)):
    if search_element==arr[i]:
        is_present=True
        break
print(is_present)


# BINARY SEARCH
elements=[8,2,10,4,3,7]
elements.sort()
search_element=int(input("Search a number: "))
low=0
upper=len(elements)-1
is_present=False
while(low<=upper):
    mid=(low+upper)//2
    if search_element==elements[mid]:
        is_present=True
        break
    elif search_element<elements[mid]:
        upper=mid-1
    elif search_element>elements[mid]:
        low=mid+1

print(is_present)