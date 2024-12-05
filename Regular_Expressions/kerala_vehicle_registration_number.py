
# Rules:

# 1.Starting with KL
# 2. 2 digit
# 3. 2 alphabets
# 4. 4 numbers
# 5. " " is inserted between rule numbers 1,2,3,4

from re import fullmatch

user_input=input("Enter vehicle number: ").upper()
pattern="KL[0-9]{2}[A-Z]{2}[0-9]{3,4}"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("Invalid")
else:
    print("Valid")



# Passport
# Adhaar Number
# Driving Licence Number