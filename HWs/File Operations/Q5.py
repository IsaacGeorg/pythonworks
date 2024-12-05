# Copy File Content:
#    - Create a program to copy content from one file to another.

fread=open("D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q5.txt","r")
fwrite=open("D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q5copy.txt","w")

for line in fread:
    fwrite.write(line)

fread.close()
fwrite.close()