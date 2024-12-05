
from re import finditer

f_read=open("D:\\vs code\\Pythonworks\\Regex_fileworks\\socialposts.txt")

for line in f_read:

    hashtags=line.rstrip("\n")

    pattern="(#)[a-zA-Z]*"

    matcher=finditer(pattern,hashtags)

    for obj in matcher:
        print(obj.group())

f_read.close()