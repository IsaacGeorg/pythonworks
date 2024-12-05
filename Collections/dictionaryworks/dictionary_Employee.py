# Create dictionary employee with keys eid, name, salary, department, experience.

employee={"eid":1045,"name":"Isaac","salary":50000,"department":"Python","experience":6}
print(employee)
print(employee["salary"])
employee["contact"]=3456789
print(employee)

if employee["experience"]>5:
    employee["salary"]=employee["salary"]+10000
else:
    employee["salary"]=employee["salary"]+5000
print(employee)

if employee["experience"]>5:
    employee["role"]="SDE"
else:
    employee["role"]="JDE"
print(employee)