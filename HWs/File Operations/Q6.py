# Find Longest Word in a File:
#    - Write a program that finds and prints the longest word in a text file.

fread=open("D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q6.txt","r")

for line in fread:
    words=line.split(" ")
    word={}
    for w in words:
        word[w]=len(w)
        wording={v:k for k,v in word.items()}
    print(wording)
        
fread.close()