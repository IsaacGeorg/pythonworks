
read="D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\words.txt"
palin="D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\palindrome.txt"

f_read=open(read,"r")
f_write=open(palin,"w")


for word in f_read:
    words=word.rstrip("\n")
    reversedword=words[::-1]
    if reversedword==words:
        f_write.write(words+"\n")

f_read.close()
f_write.close()
