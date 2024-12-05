from json import load

f=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\employee.json")

data=load(f)
for emp in data:
    print(emp)
