# Append and Display File Content:
#    - Create a program that appends user input to an existing file and then displays the entire content of the file.


append_file="D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q2.txt"
f_write=open(append_file,"a")
user_input=input("Enter anything: ")
f_write.write(user_input+"\n")
f_write.close()

read_file="D:\\vs code\\Pythonworks\\HWs\\File Operations Dataset\\Q2.txt"
f_read=open(read_file,"r")
for line in f_read:
    print(line)

f_read.close()