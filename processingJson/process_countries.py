from json import load

f=open("D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\countries.json",encoding="utf-8")

data=load(f)

# print(len(data))

all_country=[country.get("name") for country in data]
# print(all_country)

all_region=[country.get("region") for country in data]
# print(set(all_region))

region_count={region:all_region.count(region) for region in all_region}
# print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))
# print(max_region_count,region_count.get(max_region_count))

# capital of a specific country

country_capital=[country.get("capital") for country in data if country.get("name")=="India"]
# print(country_capital)


# countries with most number of borders
country_withborders={country.get("name"):len(country.get("borders",[])) for country in data}
# print(country_withborders)
max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
# print(max_border_country)


# most populated country
country_with_population=max(data,key=lambda country:country.get("population")).get("name")
# print(country_with_population)

# countries that share india borders
india_border=[country.get("borders") for country in data if country.get("name")=="India"][0]
# print(india_border)

# for code in india_border:

#     for country in data:
#         if country.get("alpha3Code")==code:
            
#              print(country.get("name"))












#  To print the translations of afghanistan and india

Afghan_indian_translations=[trans.get("translations") for trans in data if trans.get("name")=="Afghanistan" or trans.get("name")=="India"]
print(Afghan_indian_translations)


# To print the "hr" translation of India

hr_indian=[trans.get("translations").get("hr") for trans in data if trans.get("name")=="India"][0]
print(hr_indian)