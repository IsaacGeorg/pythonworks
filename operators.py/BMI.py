#Create a python program to calculate BMI 
weight_in_kg=int(input("Enter Weight in kg: "))
height_in_cm=int(input("Enter Height in cm: "))
height_in_m=height_in_cm/100
BMI=weight_in_kg/height_in_m**2
BMI=round(BMI,2)
print(f"BMI = {BMI}")