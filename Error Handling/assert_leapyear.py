

def isleapyear(year):

    if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
        return True
    else:
        return False
    


def test_is_leap_year():

    assert isleapyear(2024)==True, "leap year check failed"

    assert isleapyear(2034)==False, "invalid leap year check failed"

    assert isleapyear(2019)==False, "invalid leap year check failed"

    assert isleapyear(-2002)==False, "invalid leap year"


try:
    test_is_leap_year()
    print("test case passed")

except Exception as e:
    print("testfailed", e)






def factorial(num):
    
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

print(factorial(5))