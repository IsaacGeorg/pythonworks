from re import fullmatch
user_input=input("Enter any variable name: ")

# Rules:
# 1. Start with an alphabet(lowercase,uppercase)
# 2. any number of alphabets,digits,_

pattern="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("Invalid")
else:
    print("Valid")