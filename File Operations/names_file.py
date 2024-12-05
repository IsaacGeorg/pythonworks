

f=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\names.txt","w")

text="hello world"
languages=["python","java","c#","go"]
for l in languages:
    f.write(l+"\n")
f.write(text)     #Write method only reads string value

f.close()