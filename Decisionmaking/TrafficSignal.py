#Python program to print the signal is valid or not

# Syntax

# if condition1:
    # stmt1
# elif condition2:
    # stmt2
# elif condition3:
    # stmt3
# else:
    # stmt4

signal=input("Enter Signal: ").lower()
if signal=="red":
    print("STOP!")
elif signal=="green":
    print("GO...")
elif signal=="yellow":
    print("WAIT!!!")
else:
    print("INVALID SIGNAL")