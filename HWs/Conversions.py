#Create a python program to convert from degree celsius to FH

celsius=int(input("Enter degree celsius(C): "))
Faren=celsius*(9/5)+32
print(f"The Farenheit is {Faren}F")

#Create a python program to convert from FH to degree
celsius=(Faren-32)*(5/9)
print(f"The Celsius is {celsius}C")

#Create a python program to convert metre to centimetre
metre=int(input("Metre Range(m): "))
centi=metre*100
print(f"Centimetre => {centi}cm")

#Create a python program to convert centimetre to metre
metre=centi/100
print(f"Metre => {metre}m")

#Create a python program to convert inch to metre
inch=int(input("Inches(In): "))
met=inch*0.0254
print(f"Respected Metre is {met}m")


