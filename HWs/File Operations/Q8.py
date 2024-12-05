# Count Specific Word Occurrences:
#    - Write a program to count the occurrences of a specific word in a file.

f=open("D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q8.txt","r")

for line in f:
    line=line.casefold()
    words=line.split(" ")
    print(words)
    dict={word:words.count(word) for word in words}
    
print(dict)
f.close()