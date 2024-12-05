# Read Even Lines from a File:
#    - Create a Python program that reads and prints only the even-numbered lines from a file.

f_read=open("D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q9.txt","r")
for i,line in enumerate(f_read, start=1):
    line=line.rstrip("\n")
    if i%2==0:
        print(line)

f_read.close()