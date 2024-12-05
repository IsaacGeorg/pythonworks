employee={"id":10,"name":"ram","department":"hr","age":32,"salary":35000}
print(employee.get("department"))

employee.pop("salary")
print(employee)

for k in employee.keys():
    print(k)

for v in employee.values():
    print(v)

# fetch key and values  => items
for k,v in employee.items():
    print(k,v)

print(dir(dict))