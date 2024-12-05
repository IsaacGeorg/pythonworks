def is_palindrome(num):
    is_palindrome=True
    original=num
    digit=0
    while(num!=0):
        rem=num%10
        digit=digit*10+rem
        num=num//10
    print(digit)
    return print(is_palindrome) if digit==original else print(False)
num=int(input("Enter a number: "))
is_palindrome(num)