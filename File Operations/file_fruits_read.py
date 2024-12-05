

f=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\fruits.txt","r")

fruits=[]
for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)