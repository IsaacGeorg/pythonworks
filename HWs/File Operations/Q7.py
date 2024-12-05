# File Reverse Order:
#    - Write a program that reads a text file and displays the content in reverse order (line by line).

fread=open("D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q7.txt","r")
for line in fread:
    line=line.rstrip("\n")
    lines=line.split(" ")
    reverse=lines[::-1]

    for l in reverse:
        print(l,end=" ")

fread.close()