from re import fullmatch

user_input=input("Enter Your Driving Licence No.: ")
pattern=r"(kl|KL)[\d]{2}[ |-][0-9]{11}"

matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("Invalid")
else:
    print("Valid")