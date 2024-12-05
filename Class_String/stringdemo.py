text="Python is a powerful programming language"
split=text.split(" ")
print(split)

text="Python is a \n programming language"
word=text.strip('P')
print(word)

# lstrip()
# rstrip()
# replace()
text="Python is a \n programming language"
word=text.replace('a','e')
print(word)


text="Python programming"
print(text[:6])
print(text[12:16])
print(text[::3])
print(text[::-1])     #String Reverse



text=input("Enter string: ")
reversedstring=text[::-1]
if reversedstring == text:
    print("palindrome")
else:
    print("Not Palindrome")


text="hello"
reversedstring=""
length=len(text)-1
for i in range(length,-1,-1):
    reversedstring+=text[i]
print(reversedstring)

print(text.index("o"))



text="Vipinkumar@gmail.com"
word=text.index("@")
username=text[:word]
print(username)
print(text[0:text.index("@")])

# text="hellopython"
# print(text[:].index("0"))

