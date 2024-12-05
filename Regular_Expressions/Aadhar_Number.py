from re import fullmatch

user_input=input("Enter Aadhar Number: ")
pattern=r"[2-9][\d]{3}[ |-][\d]{4}[ |-][\d]{4}"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("Invalid")
else:
    print("Valid")