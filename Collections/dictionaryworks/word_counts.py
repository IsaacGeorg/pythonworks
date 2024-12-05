
text="ABBCAB"
wordcount={}
for ch in text:
    if ch in wordcount:
        wordcount[ch]+=1
    else:
        wordcount[ch]=1

print(wordcount)


# first recursive character B
text="ABBACB"

textcount={i:text.count(i) for i in text}
print(textcount)

words=["hello","hello","hai","this","is","this","is","hello"]
wordcount={w:words.count(w) for w in words}
recursive_element={k for k,v in wordcount.items() if v>1}
print(recursive_element)


# Maximum Recursive character

words=["hello","hai","hello",'hai','this',"is","this","hai"]
# wordcount={}

products={"apple":240,"banana":76,"mango":90,"orange":100}