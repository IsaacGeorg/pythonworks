# Q1. 
def year(user_input):
    isleapyear=True
    if((user_input%4==0 and user_input%100!=0) or(user_input%100==0 and user_input%400==0)):
        leapyear=isleapyear
    else:
        leapyear=False
    return leapyear

user_input=int(input("Enter year: "))
leap=year(user_input)
print(leap)





