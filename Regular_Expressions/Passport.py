from re import fullmatch

user_input=input("Enter Passport Number: ")
pattern=r"[A-Z][1-9]\d\s?[\d]{4}[1-9]"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("Invalid")
else:
    print("Valid")