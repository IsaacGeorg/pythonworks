
def secondlargest(*args):
    
    secondmax=sorted(args,reverse=True)
    return secondmax[1]


print(secondlargest(10,39,26,17))