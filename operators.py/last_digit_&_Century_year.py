num=int(input("Enter number: "))
last_digit=num%10
print(last_digit)

# [For odd number]
# is_odd=last_digit%2==0 
# print(is_odd)

# [For even number]
is_even=last_digit%2==0
print(is_even)

# Python program to print the year as century year
year=int(input("Enter year: "))
century_year=year%100==0
print(century_year)