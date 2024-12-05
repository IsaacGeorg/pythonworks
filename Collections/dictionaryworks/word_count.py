# text="this is a python programming interpreter interface "
# words=text.split(" ")
# print(words)

words=["hai","hello","hai","hello","hai"]
word_count={}
for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1

print(word_count)