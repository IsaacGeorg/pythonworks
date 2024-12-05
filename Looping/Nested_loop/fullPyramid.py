for row in range(1,7):
    for sp in range(1,7-row):
        print(" ",end="\t")
    for col in range(1,row+1):
        print("*",end="\t")
    for side in range(1,row):
        print("*",end="\t")
    print()


for row in range(1,7):
    a=0
    b=1
    for col in range(1,row+1):
        print(a,end="\t")
        a,b=b,a+b
    print()


