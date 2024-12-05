# Employee details:

employee={"id":100,"name":"vipin","department":"hr","salary":25000}
print(employee["name"])
print(employee["department"])

product={"id":1000,"title":"goodday","price":35,"brand":"britannia"}
print(product["brand"])
print(product["price"])

product["price"]=50
product["brand"]="parle"
print(product)
product["use-by-date"]="12-10-2024"
print(product)
product["offer"]=5
print(product)

# To check a key exist or not

if("price" in product):
    print("exist")
else:
    print("not exist")

if ("offer" in product):
    product["offer"]=20
else:
    product["offer"]=10

print(product)


