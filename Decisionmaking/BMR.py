weight=int(input("Enter your weight: "))
height=int(input("Enter your height: "))
age=int(input("Enter your age: "))
gender=input("Enter gender: ").lower()
activity_level=int(input("""
select activity level
    press 1 for sedentary
          2 for lightly active
          3 for moderatively active
          4 for very active
          5 for extra active
"""))
print(weight, height, age, gender)


if gender == "male":
    bmr=10*weight + 6.25*height - 5*age + 5

elif gender == "female":
    bmr=10*weight + 6.25*height - 5*age -161

else: 
    print("Enter valid gender.")

print(bmr)

if activity_level==1:
    calorie=bmr*1.2

elif activity_level==2:
    calorie=bmr*1.375

elif activity_level==3:
    calorie=bmr*1.55

elif activity_level==4:
    calorie=bmr*1.725

elif activity_level==5:
    calorie=bmr*1.9

else:
    print("Select valid choice of activity level...!!!")

print(f"The average calorie intake for a {gender} is {calorie}kcal")

target_weight= int(input("Enter the weight to reduce in kg: "))
duration=int(input("Enter the number of weeks as duration: "))

# 1kg => 7700

calorie_deficit=target_weight*7700
days=duration*7
dailycalorie=calorie_deficit/days

print(calorie_deficit)
print(days)
print(dailycalorie)