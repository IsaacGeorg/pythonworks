box=[
    {"color":"green","size":2},
    {"color":"blue","size":5},
    {"color":"red","size":8},
    {"color":"yellow","size":3},
    {"color":"green","size":7},
    
]
print(len(box))


for b in box:
    print(b.get("color"))
    if b.get("size")==3:
        print(b.get("color"))