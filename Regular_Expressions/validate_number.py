# from re import fullmatch
# user_input=input("Date: ")
# pattern="[1-9]|0[1-9]|1[0-2]"
# matcher=fullmatch(pattern,user_input)
# if matcher==None:
#     print("Invalid")
# else:
#     print("Valid")


# Program for validating date
# 01 1 31
# from re import fullmatch
# user_input=input("Date: ")
# pattern="0?[1-9]|[12][0-9]|3[01]"                   # ? means optional
# matcher=fullmatch(pattern,user_input)
# if matcher==None:
#     print("Invalid")
# else:
#     print("Valid")


# Program for validating calender
# from re import fullmatch
# user_input=input("Date: ")
# pattern="0[1-9]|[1-9]|3[01]|1[0-9]|2[0-9]"
# matcher=fullmatch(pattern,user_input)
# if matcher==None:
#     print("Invalid")
# else:
#     print("Valid")



# validate years from 1800 to 2024
from re import fullmatch
user_input=input("year: ")
pattern="(18|19)[0-9]{2}|20[01][0-9]|202[0-4]"
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("Invalid")
else:
    print("Valid")

    
