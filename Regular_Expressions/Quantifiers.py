from re import finditer
text="abababaaababaabbbab"
# pattern="a{2}"                    # find the iteration of a having repitition=2
pattern="a{1,3}"
matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())