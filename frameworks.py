print("python=> Django,flask")
print("java=>spring")
print("dart=>Flutter")
print("php=>Laravel")


text="this is a carr."
text1=text.split()
def length(w):
    return len(w)
srt=sorted(text1, key=length, reverse=True)
print(srt)

orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]
itemsummary={}
for item in orders:
    if item in itemsummary:
        itemsummary[item]+=1
    else:
        itemsummary[item]=1

print(itemsummary)



text="uhhewbjneehnjnrhnd vhsjvbh"
dict1={i:text.count(i) for i in text}
print(dict1)


sourceword="CHICKENN"
targetword="HEN"
characters={i:sourceword.count(i) for i in sourceword for j in targetword if i==j}
print(characters)
