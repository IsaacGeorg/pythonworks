expenses=[15000,12000,13000,11000,12000]
duplicate=[]
for i in expenses:
    if expenses.count(i)>1 and i not in duplicate:
        duplicate=duplicate+[i]
        
if duplicate:
    print("The duplicate element:",duplicate)
else:
    print("No frequent duplicates..")
