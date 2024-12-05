
f=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\frameworks.txt","a")

framework=["springboot","oodo","fastapi"]

for fw in framework:
    f.write(fw+"\n")

f.close()