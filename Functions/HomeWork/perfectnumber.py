def is_perfect_number(num):
    total=0
    original=num
    for i in range(1,num):
        if num%i==0:
            total=total+i
    print(total)
    return print(True) if original==total else print(False)

num=int(input("Enter a number: "))
is_perfect_number(num)