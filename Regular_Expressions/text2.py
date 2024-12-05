
# Print the output to find the where a alphabet or number is present or not.

from re import finditer

text=("I have 3 cars,2 bike and 1 Cycle")
pattern="[0-9]"                                 # either "3" or "2" or "1"
num_match=finditer(pattern,text)
# for num in num_match:
    # print(num.start(),num.group())

pattern="[a-zA-Z]"                              # either a to z or A to Z
alpha=finditer(pattern,text)
# for al in alpha:
    # print(al.start(),al.group())


# Check for all alphanumerics
pattern="[a-zA-Z0-9]"
alphanum=finditer(pattern,text)
# for all in alphanum:
    # print([all.start(),all.group()],end="")


pattern="[^ak]"# exclude a, k
exclude=finditer(pattern,text)
# for all in exclude:
    # print(all.start(),all.group())


# all lowercase alphabets exclude a,k

# pattern="[^akA-Z0-9,\- ]"
exclude=finditer(pattern,text)
# for all in exclude:
    # print(all.start(),all.group())

# Check for all special characters

text1="jn 3n1!$2@ jneal"
pattern="[^a-zA-Z0-9 ]"
special=finditer(pattern,text1)
for char in special:
    print(char.start(),char.group())

