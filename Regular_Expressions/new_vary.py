
from re import fullmatch
user_input=input("Enter variable name: ")
pattern="[p-tP-T][369][a-zA-Z0-9@]*"
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("Invalid")
else:
    print("valid")