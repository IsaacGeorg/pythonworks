users=["rahul","rohit","kohli","rishab","pandya","siraj","sanju"]
rahul_followers=["rohit","kohli","rishab"]
user=set(users)
user.remove("rahul")
rahul=set(rahul_followers)
Not_followers=user.difference(rahul)
print(Not_followers)

sanju_followers=["sanju","rohit","kohli"]
sanju=set(sanju_followers)
mutualfriends=rahul.intersection(sanju)
print(mutualfriends)