


# source_word="silent"  heart
# target_word="listen"  earth

source_word=input("Enter string1: ")
target_word=input("Enter string2: ")
is_anagram=True
for ch in source_word:
    if ch not in target_word:
        is_anagram=False
        break
print(is_anagram)



#String
source_word="silent"
word=source_word[::-1]
print(word)