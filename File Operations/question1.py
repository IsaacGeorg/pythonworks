
f=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\question1.txt","r")

words=[]


for line in f:

    line=line.rstrip("\n")
    allwords=line.split(" ")

    for w in allwords:
        
        words.append(w)

print(words)

word_count={w:words.count(w) for w in words}
print(word_count)

value_key=[[v,k] for k,v in word_count.items()]
print(sorted(value_key,reverse=True))
