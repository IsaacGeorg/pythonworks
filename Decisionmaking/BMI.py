#BMI = weight in kg/(height in metre)**2

weight_in_kg=int(input("Enter weight: "))
height_in_cm=int(input("Enter height: "))
height_in_m=height_in_cm/100

bmi=weight_in_kg/(height_in_m)**2
print(bmi)
round(bmi,0)

if bmi<19:                               #bmi<19
    print("Underweight")
elif bmi<25:                             #19>=bmi<25
    print("Normalweight")
elif bmi<30:                             #25>=bmi<30
    print("Normalweight")
elif bmi>=30:                            #bmi>=30
    print("Obesity")
