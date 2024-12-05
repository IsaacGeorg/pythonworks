

def vote(rating):

    if rating<0:
        raise Exception("too low")
    elif rating>10:
        raise Exception("too high")
    else:
        print("Done.")
try:
    vote(18)
except Exception as e:
    print(e)

print("Hello")

print("Next Operation..")