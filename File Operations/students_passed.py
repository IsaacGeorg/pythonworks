

all=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\allstudents.txt","r")
failed=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\failed.txt","r")

allstudents_set=set()
failed_set=set()

for i in all:
    i=i.rstrip("\n")
    allstudents_set.add(i)
print("All students: ",allstudents_set)

for j in failed:
    j=j.rstrip("\n")
    failed_set.add(j)
print("Failed: ",failed_set)

passed=allstudents_set.difference(failed_set)
print("Students passed: ",passed)


