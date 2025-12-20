#this game gueeses a random no. between 0 to 100
import random
y= random.randint (0,100)
x= int (input (" guess a number between 0 to 100"))
while (x!=y):
    if (x<0 or x>100):
        print ("number is out of range")
        x= int(input ("Enter another number"))
    else:
        if (x<y):
            x= int (input ("Guess a bigger number"))
        elif (x>y):
            x= int (input ("Guess a smaller number"))
print ("You guessed the number")
