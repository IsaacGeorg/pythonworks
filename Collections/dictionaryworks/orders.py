
# Taking item order

orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]
itemsummary={}
for item in orders:
    if item in itemsummary:
        itemsummary[item]+=1
    else:
        itemsummary[item]=1

print(itemsummary)