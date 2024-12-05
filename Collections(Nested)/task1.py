lst=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    10
]

# Using for loop
list_objects=[]
for item in lst:
    if isinstance(item,list):
        list_objects.append(item)
print(list_objects)

# Using list comprehension
listobject=[item for item in lst if isinstance(item,list)]
print(listobject)

# Maximum length of list in listobject
print(max(listobject,key=len))