arr=[10,20,30,40,2,3]
result={}
for i in arr:
    square=i**2
    result[i]=square
print(result)


# Dictionary Comprehension

arr=[10,20,30,40,2,3]
result={num:num**3 for num in arr}
print(result)

# even&odd={}
evennum={}
oddnum={}
for num in arr:
    if num%2==0:
        evennum[num]=num**3
    else:
        oddnum[num]=num**3

print(oddnum,evennum)

arr=[10,20,30,40,2,3,7,8,9,10,30]

frequencycount={num:arr.count(num) for num in arr}
print(frequencycount)

text="ABDGSVAANSGABABHNCBXN"
characterfrequency={num:text.count(num) for num in text}
print(characterfrequency)

for k,v in characterfrequency.items():
    if v==1:
        print(k,v)

nonrecursive={k for k,v in characterfrequency.items() if v==1}
print(nonrecursive)