from re import fullmatch

user_input=input("Enter number: ")
pattern=r"[A-Z]{3}[PCAFHT][A-Z]{1}[\d]{4}[A-Z]"

matcher=fullmatch(pattern,user_input)

if matcher== None:
    print("Invalid")
else:
    print("Valid")