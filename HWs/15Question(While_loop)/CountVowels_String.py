#Q14. Write a python program to count the number of vowels in a string using a 'while' loop.

# Input string
input_string = "Hello, World!"

# Convert the string to lowercase to make the vowel check case-insensitive
input_string = input_string.lower()

# Vowel set
vowels = "aeiou"

# Initialize the vowel count
vowel_count = 0

# Initialize the index for the while loop
index = 0

# Loop through the string
while index < len(input_string):
    # Check if the current character is a vowel
    if input_string[index] in vowels:
        vowel_count += 1
    # Move to the next character
    index += 1

# Print the result
print("Number of vowels:", vowel_count)
