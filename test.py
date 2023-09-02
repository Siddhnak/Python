# Guessing game using random until the ans is correct

import random



def Ggame():
    rno=print(random.randint(1,14))
    guess=0

    
    while guess!=rno:
        # guess=int(input)
        guess = int(input("enter your guess"))
        print("That's not a correct option")

    
    print("you are correct")


Ggame()