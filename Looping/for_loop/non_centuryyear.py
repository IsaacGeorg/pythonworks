#1800 to 2024
print("Non Century years: ")
for year in range(1800,2025,1):
    if year%100!=0:
        print(year)

print("Century Years: ")
for year in range(1800,2025,1):
    if year%100==0:
        print(year)