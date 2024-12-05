
f=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\years.txt","w")

for year in range(1800,2025):
    f.write(str(year)+"\n")

f.close()