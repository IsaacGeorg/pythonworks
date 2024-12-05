#Write a program to print leapyear or not

year=int(input("Enter an year: "))
if ((year%4==0 and year%100!=0) or (year%100==0 and year%400==0)):
    print("Leap year")
else:
    print("Not leap year")
