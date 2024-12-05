
from re import findall

f=open("D:\\vs code\\Pythonworks\\Regex_fileworks\\url.txt")

content=f.read()

pattern="https?://[\w./]+"                  # + operator matches one or more occurrences of the preceding character or group

urls=findall(pattern,content)

for url in urls:
    print(url)