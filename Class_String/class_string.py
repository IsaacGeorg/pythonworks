# class object:
#     #attributes
#     #methods



# class Fan:

#     color:  # attributes
#     speed:
#     shape:
#     weight:


#     def switch_on():
#         pass
# 
#     def rotate():
#         pass


# class car:

#     color:
#     shape:
#     engine:

#     def start():
#         pass
#     def stop():
#         pass
    

# balenocar=car.start()



# referencename=Classname()  #object

    # def capitalize()
    # def casefold()
    # def isalpha()
    #def isdigit()
    # def isalnum()
    # def startswith(str)
    # def endswith(str)

text="helloWorld"
result=text.capitalize()
print(result)
print(text.casefold())
print(text.isalnum())
print(text.startswith("he"))
print(text.endswith("d"))

for ch in text:
    print(ch)


text="hellopython"
text1=text.casefold()
for i in text:
    if (i=='a' or i=="e" or i=="o" or i=="i" or i=="u"):
        print(i)       


text="pneumonoultramicroscopicsilicovolcanoconiosis"
text=text.casefold()
vowel_sequence=("a","e","i","o","u")
vowels=0
consonants=0
for i in text:
    if i in vowel_sequence:
        vowels=vowels+1
    else:
        consonants=consonants+1

print(vowels)
print(consonants)

text="The quick brown fox jumps over the lazy dog"
alphabet="abcdefghijklmnopqrstuvwxyz"
is_Pangram=True
for ch in alphabet:
    if ch not in text:
        is_Pangram=False

        break
print(is_Pangram)