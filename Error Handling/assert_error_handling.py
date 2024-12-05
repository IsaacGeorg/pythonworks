
def poll(age):

    assert age>18 ,"invalid age"

    print("voted")

try:
    poll(7)

except Exception as e:
    print(e)



def review(rating):

    assert rating>0, "too low"

    assert rating in range(0,11),"too high"

    print("rated")

review(7)