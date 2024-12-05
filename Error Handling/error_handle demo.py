
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# try:
#     result=num1/num2


#     print(result)
# except:
#     print("Error Occured!!")

# print("File write")
# print("Database Commit")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
try:
    result=num1/num2
    print(result)
# except Exception as e:
#     print(e)
#     num2=int(input("Enter number2: "))
#     result=num1/num2
#     print(result)

finally:
    print("File write")
    print("Database Commit")