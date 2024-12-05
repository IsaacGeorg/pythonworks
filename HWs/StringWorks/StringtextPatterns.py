# Input:
# PQRS
# ABCD
# Output:
# PAQBRCSD


text1="PQRS"
text2="ABCD"
print(text1)
print(text2)
word=""

for i,j in zip(text1,text2):
    word=word+i+j

print(word)


# OR


# str1="PQRS"
# str2="ABCD"

# result=""
# smallesttext=text1 if text1>text2 else text2

# for char in range(0, len(smallesttext)):
#     result+=str1[i]
# print(result)
# Input:
# PQRST
# ABC
# Output:
# PAQBRCST





text1="PQRST"
text2="ABC"
print(text1)
print(text2)
word=""
# tim=text1.replace(" ",text2)
# print(tim)
for i,j in zip(text1,text2):
    word=word+i+j
word += text1[len(text2):] + text2[len(text1):]
print(word)


# text="ABCABC"
# print the first recursive character - A

text="ABCABC"
for i in text:
    if text=="A":
        print(i)