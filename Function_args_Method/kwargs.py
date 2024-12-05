
def display_mobiledata(**kwargs):

    print(kwargs.get("name"))

display_mobiledata(name="oneplus",price=320000,display="amoled")



# Calculator ==> args and kwargs parameter implementation
def calculator(*args,**kwargs):

    if kwargs.get("operator")=="+":
        return sum(args)
    
    if kwargs.get('operator')=="*":
        result=1
        for num in args:
            result=result*num
        return result

print(calculator(10,20,30,operator="+"))
print(calculator(10,20,30,operator="*"))


# Student_info

def student_info(*args,**kwargs):

    if kwargs.get("operation")=="avg":
        avg=sum(args)/len(args)
        return avg
    
    if kwargs.get("operation")=="total":
        total=sum(args)
        return total


print(student_info(40,30,43,operation="avg"))
print(student_info(40,30,43,operation="total"))



# sorting in ascending and descending order

def sorting(*args,**kwargs):

    if kwargs.get("reverse")==True:
        sort=sorted(args,reverse=True)
        return sort
    
    if kwargs.get("reverse")==False:
        sort=sorted(args)
        return sort
    
    

print(sorting(28,56,15,34,67,45,reverse=True))
print(sorting(28,56,15,34,67,45,reverse=False))