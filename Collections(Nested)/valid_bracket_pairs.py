userinput=input("input: ")
symbol_dictionary={
    "{":"}",
    "[":"]",
    "(":")",
    "<":">",
}

symbol_stack=[]
top=-1

isvalid=True

for symbol in userinput:
    if symbol in symbol_dictionary:
        top=top+1
        symbol_stack.append(symbol)
    elif top==-1:
        isvalid=False
    elif symbol==symbol_dictionary.get(symbol_stack[top]):
        top=top-1
        symbol_stack.pop()
    else:
        isvalid=False

if len(symbol_stack)==0:
    print("valid")
else:
    print("invalid")


lst1=["apple","mango","onion","potatto"]
lst2=[100,200]

# Output: {"apple":100,"mango":200,"onion":1,"potatto":2}



