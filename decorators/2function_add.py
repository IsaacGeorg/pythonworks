def decorator(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper


def round_dec(fn):
    def wrapper(num1,num2):
        num1=round(num1)
        num2=round(num2)
        return fn(num1,num2)
    return wrapper

@round_dec
@decorator
def addnumber(num1,num2):

    return num1+num2

@round_dec
@decorator
def subtraction(num1,num2):

    return num1-num2

@round_dec
@decorator
def division(num1,num2):

    return (num1/num2)


print(addnumber(5.6,35.4))
print(subtraction(5.5,3.5))
print(division(5.4,35.2))
