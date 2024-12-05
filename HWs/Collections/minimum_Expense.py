expenses=[15000,12000,13000,11000,9000,12500,430,600]
i=0
prev_exp=expenses[i]
for exp in expenses:
    if prev_exp==exp:
        i=i+1
        # print("Cannot be Determined")
    if prev_exp>exp:
        prev_exp=exp
    else:
        prev_exp=prev_exp

print("Minimum Expense:", prev_exp)
        