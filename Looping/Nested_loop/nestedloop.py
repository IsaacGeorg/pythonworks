for row in range(1,7):
    for column in range(1,row+1):
        print("*", end="\t")
    print()

#pattern2
#1
#2 2 
#3 3 3
#4 4 4 4

for row in range(1,6):
    for column in range(1,row+1):
        print(row, end="\t")
    print()

for row in range(1,6):
    for column in range(1,row+1):
        print(column, end="\t")
    print()

for row in range(6,1,-1):
    for column in range(1,row+1):
        print(column, end="\t")
    print()

for row in range(6,0,-1):
    for column in range(1,row):
        print("*", end="\t")
    print()


for row in range(6,0,-1):
    for col in range(1,row+1):
        if col==1 or col==row or row==6:
            print("*",end="\t")
        else:
            print(" ", end="\t")
    print()


for row in range(6,0,-1):
    for col in range(row+5,0,-1):
        # if col==1 or col==row or row==6:
            print("*",end="\t")
        # else:
        #     print(" ", end="\t")
    print()


for row in range(1,7):
    for col in range(1,row+1):
        print(row,end="\t")
    print()