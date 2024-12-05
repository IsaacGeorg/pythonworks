st=set()
print(type(st))
st={10,20,30,30,40,10,50}
print(st)

colors={"red","green","blue"}
colors.add("yellow")
print(colors)

arr=[10,10,20,30,40,50,40]  # Input Array
st=set()         # Creating Empty set
for i in arr:      # Iterate array
    st.add(i)       # Adding elements of arr to set, st.
print(st)           # Display set



# Intersection of set
set1={10,30,20,50,40}
set2={30,10,60,25}
intersection_set=set1.intersection(set2)
print(intersection_set)

# Union of set
union_set=set1.union(set2)
print(union_set)

# Difference Set
difference_set=set1.difference(set2)
print(difference_set)


# Remove an element from set, st
st={10,40,28,30,50}
st.remove(28)
print(st)


st={10,20,30}
st2={10,40,20,30,50}
print(st.issubset(st2))
print(st2.issuperset(st))
print(st.isdisjoint(st2))
st={10,20,30,100,80}
st2={10,40,20,30,50}
print(st.symmetric_difference(st2))

st.update(st2)
print(st)

text="this is a test to remove duplicate words this test is simple"
test=text.split(" ")
print(set(test))

text2="this simple test remove duplicate words"
test1=text2.split(" ")
test2=set(test1)
print(test2.issubset(test))

