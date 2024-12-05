studentdata={
    "hari":[10,20,30],
    "vipin":[17,28,30],
    "karnan":[80,50,63],
    "anver":[109,20,30],
    "majo":[10,90,30]
}
index=1
for i,item in enumerate(studentdata):
    if i+1==index:
        marks=studentdata.get(item)
        avg=sum(marks)/len(marks)
        print(avg)


# student=[k:(sum(v)/len(v)) for k,v in studentdata.items() i]
# print(student)




# kangaroo word

source="TARGET"
word="GET"

ispresent={True for i in source if i in word} 
print(ispresent)