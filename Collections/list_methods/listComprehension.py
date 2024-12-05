
# LIST COMPREHENSION
arr=[2,3,4,5,6,7]

# [return loop condition]
add=[num+5 for num in arr]
print(add)
squares=[num**2 for num in arr]
print(squares)


# mapping
# filtering
# reduce

# filtering
even_number=[num for num in arr if num%2==0]
print(even_number)

gt_five=[num for num in arr if num>5]
print(gt_five)

map_num=[num+1 if num>5 else num-1 for num in arr]
print(map_num)

text=["apple","iphone","orange","potatto"]

words=[i for i in text if i[0] in ["a","e","i","o","u"] ]
print(words)

consonant=[i for i in text if i[0] not in ["a","e","i","o","u"]]
print(consonant)

long=max([len(w) for w in text])
longest_words=[w for w in text if len(w)==long]
print(longest_words)