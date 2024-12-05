# lambda function

products={"apple":240,"orange":70,"grapes":120,"banana":100}
swap={v:k for k,v in products.items()}
print(max(swap))

sub=lambda n1,n2:n1-n2
print(sub(10,2))

add=lambda n1,n2:n1+n2
print(add(9,23))

cube=lambda n:n**3
print(cube(5))


string_maxtwo=lambda str1,str2: str1 if len(str1)>len(str2) else str2
print(string_maxtwo("nhsdhn","gtxguyhnd"))


smart_sub=lambda num1,num2: num1-num2 if num1>num2 else num2-num1
print(smart_sub(38,55))


words=["hello","hai","morning","test"]
def get_length(word):
    return len(word)
print(max(words,key=get_length))


text="this is a simple programming question"
text1=text.split()
def get_length(w):
    return len(w)
srt_words=sorted(text1,key=get_length,reverse=True)
print(srt_words)


cube=lambda num:num**3
print(cube(6))


text="this is a carr..."
text1=text.split(" ")
def length(w):
    return len(w)
srt=sorted(text1,key=length,reverse=True)
print(srt)