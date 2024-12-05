
from re import findall

f=open("D:\\vs code\\Pythonworks\\Regex_fileworks\\data.txt")

content=f.read()
pattern=r"[\d]{2}/[\d]{2}/[\d]{4}"

dates=findall(pattern,content)
for date in dates:
    print(date)