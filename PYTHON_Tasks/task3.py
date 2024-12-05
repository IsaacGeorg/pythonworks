roman=input("Enter Roman Letter: ")
length=len(roman)
diction={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
count=0

for i in range(length):
    
    if i + 1 < length and diction[roman[i]] < diction[roman[i + 1]]:
        count -= diction[roman[i]] 
    else:
        count += diction[roman[i]]  

print(count)