# 1.

text="On June 5th, 2024, we will celebrate @ our annual event: 'Tech Innovation 2024!'"
words=text.lower()

alphabets_count = sum(c.isalpha() for c in text)

spaces_count = text.count(" ")

numbers_count = sum(c.isdigit() for c in text)

print(f"Alphabets count: {alphabets_count}")
print(f"Spaces count: {spaces_count}")
print(f"Numbers count: {numbers_count}")


#2.
text = "this is a simple question return word with maximum number of characters"
max_word = max(text.split(), key=len)
print(f"Word with maximum number of characters: {max_word}")



# 3. given a string

text = "this is a simple python program that print most recursive word . this program is simple" 

# write a program to print most frequent word
words=text.split(" ")
for word in words:
    i=words.count(word)
    print(i)


# list
#1.

lst=[12,35,4,35,12]
reverse=lst[::-1]
if lst==reverse:
    print(True)
else:
    print(False)



# dictionary

#4.
dict={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",11:"XI",12:"XII",13:"XIII",14:"XIV",15:"XV"}

user_input=int(input("Enter number: "))
if user_input in dict:
    print(dict.get(user_input))
else:
    print("Enter valid number")