source_word="CHIKENN"
target_word="HEN"
# character_count={}
# for ch in source_word:

#     if ch in character_count:
#         character_count[ch]=character_count[ch]+1
#     else:
#         character_count[ch]=1


# print(character_count)


character_count={ch:source_word.count(ch) for ch in source_word}
print(character_count)

iskangaroo=True

for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]-=1
    else:
        iskangaroo=False
        break

print(iskangaroo)




sample_input=input("Enter brackets: ")
# hipe=sample_input.split(" ")
# print(hipe)
for i in range(0,len(sample_input)):
    for j in range(i+1,len(sample_input)):
        if i==j:
            print("valid")
            break
        else:
            print("not valid")


    # j=i+1
    # if sample_input[i]==sample_input[j]:
    #     print("valid")
    # else:
    #     print("not valid")




