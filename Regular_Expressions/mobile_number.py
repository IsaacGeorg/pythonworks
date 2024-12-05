
# Rules:
# 1.first letter7,8,9
# 2.any 9 digits
# 3.the full number must have 10 digits

from re import fullmatch

user_input=input("Mobile number:")

pattern="(91)+[789][0-9]{9}"                      # ? ==> means optional
                                                    # + means must be there

matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("Invalid")
else:
    print("valid")