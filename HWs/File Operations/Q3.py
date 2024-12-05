# Word Count in a File:
#    - Write a program to count the number of words in a given text file.

fread=open("D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q3.txt","r")
for s in fread:
    print(len(s))

fread.close()