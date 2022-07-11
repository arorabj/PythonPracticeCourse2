import random

highest=1000
lowest=1
answer = random.randint(lowest,highest)

guess =  int(input("Guess any random number between 1, 1000"))
print (answer)
while True :

    if guess == answer :
        print ("You have guessed it right")
        break

    elif guess > answer:
        highest = guess
        guess = int(input("Guess the number between {}, {} as your no. is smaller than previous guess :".format(lowest,highest)))
        # pass does nothing
        pass

    elif guess < answer:
        lowest = guess
        guess = int(input("Guess any random number between {},{} as your no. is larger than previous guess:".format(lowest,highest)))
        # pass does nothing
        pass

