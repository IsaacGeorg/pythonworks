num=int(input("Enter number:"))
prev=0
curr=1
is_fibo=False
print(prev)
print(curr)
for i in range(1,10):
    next=prev+curr
    prev=curr
    curr=next
    if next==num:

        is_fibo=True

        break

print(is_fibo)

