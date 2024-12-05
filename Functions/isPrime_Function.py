def is_Prime(num1):
    
    for i in range(2,num1):
        if num1%i==0:
            Prime=False
            break
        else:
            Prime=True
    print(Prime)
    return

is_Prime(66)
Prime=True
        