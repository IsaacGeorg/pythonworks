from re import finditer

text="fatcatrunsveryfasttocaththerat"
pattern="at"
matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())
    
