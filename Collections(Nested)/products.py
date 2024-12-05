

products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900},
    {"id":9,"title":"iphone16pro+","brand":"apple","price":150000}


]

# total number of mobiles
print(len(products))
# print mobile titles
mobile=[p.get("title") for p in products]
print(mobile)
# print samsung mobiles
brand=[p.get("title") for p in products if p.get("brand")=="samsung"]
print(brand)

# To get the maximum price of dictionary named products
print(max(products,key= lambda p:p.get("price")))


# To get the minimum price of dictionary named products
print(min(products,key= lambda p:p.get("price")))


#  If the value of the products having same price and want to print the names of both.
highest_price=max(products,key=lambda p:p.get("price"))
highest=highest_price.get("price")
costly_mobiles=[m.get("title") for m in products if m.get("price")==highest]
print(costly_mobiles)

# Count of Samsung mobiles

mob=[m for m in products if m.get("brand")=="samsung"]
print(len(mob))


allbrands=[p.get("brand") for p in products]
all={b:allbrands.count(b) for b in allbrands}
print(all)
