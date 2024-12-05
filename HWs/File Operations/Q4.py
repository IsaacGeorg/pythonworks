# Line Count in a File:
#    - Write a Python program that reads a file and prints the total number of lines in the file.

fread=open("D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q4.txt","r")
count=0
for line in fread:
    
    count=count+1

print(f"Number of lines: {count}")

fread.close()

