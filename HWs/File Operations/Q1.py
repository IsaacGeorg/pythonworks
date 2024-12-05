# Write and Read a File:
#    - Write a program to take input from the user and write it to a file. Then, read the content from the file and display it.


write="D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q1.txt"

f_write=open(write,"w")
user_input=input("Content: ")
f_write.write(user_input)
f_write.close()

read="D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q1.txt"
f_read=open(read,"r")
for line in f_read:
    print(line)

f_read.close()

