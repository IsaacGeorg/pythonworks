# class list:

#    def append(self):
#    def pop(self or position):
#    def insert(position, element)
#    def index(element)
#    def copy()
#    def sort() 

# append() => inserting an element at the end of the list.
# pop()    => removing or popping element from the end of the list.
# insert() => inserting an element at a specified position.
# index()  => To get the index of the element present in the list.
# copy()   => To get the copy of the list.
# sort()   => To sort the list in Ascending Order.


colors=["red","yellow","green"]
colors.append("blue")
print(colors)

colors=["red","green","blue"]
popped=colors.pop()
print(colors,"\n", f"{popped} is the popped element of list colors")

colors=["red","green","blue"]
popped=colors.pop(1)
print(colors,"\n", f"{popped} is the popped element of list colors")

colors=["red","green","blue"]
colors.insert(0,"purple")
print(colors)


# Rotating elements in the list

arr=[100,200,300,400,500]
k=2
for i in range(0,k):
    popped=arr.pop()
    arr.insert(0,popped)
print(arr)



red_index=colors.index("red")
print(red_index)

color_list=["red","orange","yellow","white","grey"]
color_list2=color_list.copy()
color_list2.pop()
print(color_list2)
print(color_list)
numbered=[{index:val} for index,val in enumerate(color_list)]
print(numbered)
# Sorting in ascending Order

lst=[3,4,2,5,2,6,5]
lst.sort()
print(lst)

# Sorting in Descending Order
lst=[2,5,3,8,4,7,2]
lst.sort(reverse=True)
print(lst)