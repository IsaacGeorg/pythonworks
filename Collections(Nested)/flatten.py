arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]
]

flat_lst=[num for ls in arr for num in ls]
print(flat_lst)

flat_lst=[num for ls in arr for num in ls if num>25]
print(flat_lst)