import random
print ("Number Guessing Game")
number = random.randint(1,9)
chances = 0 
print ("Guess a number beetween 1 and 9 :  ")
while chances<5:
    guess = int(input("Enter Your Guess : "))
    if guess==number:
        print ("Congrats You Won")
        break
    elif guess<number:
        print("The guess is very low: Try guessing a number higher than this", guess)
    else:
        print ("Guess was too high !: Guess number lower than this", guess)
    chances+=1
if not chances<5:
    print ("You lose : The number was : ", number)
