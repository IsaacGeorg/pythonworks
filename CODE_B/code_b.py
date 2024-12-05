# Q1. Write a python program that reads three numbers num1,num2 and num3 from the user and prints the second largest number among them
#       without using any builtin functions like max(), min() or sorting functions.

num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))

if num1>num2 and num1>num3:
    if num2>num3:
        print(f"The second largest: {num2}")
    else:
        print(f"The second largest number: {num3}")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"The second largest is {num1}")
    else:
        print(f"The second largest: {num3}")
elif num3>num2 and num3>num1:
    if num2>num1:
        print(f"The second largest: {num2}")
    else:
        print(f"The second largest: {num1}")
else:
    print("Enter a valid number...")


# Q2. Count Vowels in a string:

def count_vowels(string):
    counter={ch:string.count(ch) for ch in string if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"}
    print(counter)
    return 

string=input("Enter the string:")
count_vowels(string)


# Q3. text="Hello world! This is a test. Hello everyone."

def non_recursive_words(text):
    character=[]
    for ch in range(0,len(text)):
        if text[ch]!="!" and text[ch]!="." and text[ch]!="?" and text[ch]!="," and text[ch]!=";":
            character.append(text[ch])
            
            print(character)
            
    return 

text=input("Text: ").casefold()
non_recursive_words(text)
