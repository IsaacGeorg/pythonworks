# Q11. Write a python program that asks the user to guess a number between 1 and 10 until they get it right using a 'While' loop.

from random import randint as rt
g=rt(1,11)
while True:
    user=int(input("Guess a number: "))
    if g==user:
        print("Well Guessed!")
        break
    else:
        print("Incorrect\n")
    