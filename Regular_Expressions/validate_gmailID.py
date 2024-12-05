from re import fullmatch

user_input=input("Enter Email id: ")
pattern="[a-z]+[a-z0-9]{5,64}(@gmail.com)"

matcher=fullmatch(pattern,user_input)

print("Invalid" if matcher==None else "Valid")



# regular expression is also used for web scraping