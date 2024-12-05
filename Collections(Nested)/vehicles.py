cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]

# Total number of cars:
print(f"Total cars=>{len(cars)}")

# print available colors of baleno

baleno_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"]
print(baleno_colors[0])

# print all brands, no duplicates allowed
car_brands=set(c.get("brand") for c in cars)
print(car_brands)

# Print car names available in amt transmission
amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt_cars)

# cars available in blue color
blue_car=[c.get("name") for c in cars if "blue" in c.get("colors")]
print(blue_car)

# print all transmissions
car_transmission={t for c in cars for t in c.get("transmissions")}
print(car_transmission)

# print all colors
car_colors={col for c in cars for col in c.get("colors")}
print(car_colors)


# most popular color
car_colors=[col for c in cars for col in c.get("colors")]


# costly car
costly=max(cars, key=lambda c:c.get("price"))
print(costly.get("name"))                #For getting name only in the list.

# car with minimum cost
mincost=min(cars, key=lambda c:c.get("price"))
print(mincost.get("name"))

# sort cars with price
carwith_price=sorted(cars,key=lambda d:d.get("price"),reverse=True)
car={c.get("name"):c.get("price") for c in carwith_price}
print(car)


# price,brand,car_transmission
carprice=sorted(cars,key=lambda c:c.get("price"))
carlist={c.get("name"):[c.get("price"),c.get("brand"),c.get("transmissions")] for c in carprice}
print(carlist)