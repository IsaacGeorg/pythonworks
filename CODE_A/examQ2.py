def most_frequent_word(text):
    text.split(" ")
    for i in range(len(text)):

        

        if text[i]!="!" and text[i]!=".":
            # i=i+1
            test=""+str(text[i])
            print((test),end="")

    return

text=input("text: ").casefold()
most_frequent_word(text)