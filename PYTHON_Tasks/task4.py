s=input()
t=input()

i=0

for char in t:
    if i<len(s) and char==s[i]:
        i=i+1

if i==len(s):
    print(True)
else:
    print(False)
