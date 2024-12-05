
#Example 1
word1="abc"
word2="pqr"
merge=[]
for i, j in zip(word1,word2):
    merge.append(i)
    merge.append(j)

print(merge)

#Example 2
word1="ab"
word2="pqrs"
merge=[]
for i, j in zip(word1,word2):
    merge.append(i)
    merge.append(j)

merge.extend(word2[len(word1):])
print(merge)