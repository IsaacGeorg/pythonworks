def is_perfect_number(num):
    is_perfect_number=True
    original=num
    length=len(str(num))
    digit=0
    while(num!=0):
        rem=num%10
        result=rem**length
        digit=digit+result
        num=num//10
    print(digit)
    return print(is_perfect_number) if digit==original else print(False)
num=int(input("Enter a number: "))
is_perfect_number(num)
