
from re import fullmatch

f_read=open("D:\\vs code\\Pythonworks\\Regex_fileworks\\phone_numbers.txt")

for line in f_read:

    read=line.rstrip("\n")
    pattern=r"(91)?[\d]{10}"

    matcher=fullmatch(pattern,read)
    if matcher!=None:
        print(read)

f_read.close()