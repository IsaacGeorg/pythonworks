from re import finditer
text="I have 3cars,2bikes and 1 Cycle"
# pattern=r"\w"                            # \w ==> [a-zA-Z0-9]    alphanumerics
# pattern="\d"                               # \d ==> [0-9]           digits
# pattern="\D"                                #\D  ==> [^0-9]       excluding digits
# pattern="\W"                                    #\W ==> [^a-zA-Z0-9]    special characters
# pattern="\s"                                        # \s ==> space
pattern="\S"                                            # \S ==>exclude space
alphanumeric=finditer(pattern,text)

for obj in alphanumeric:
    print(obj.start(),obj.group())
