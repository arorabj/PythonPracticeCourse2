low =1
high = 1000

print ("Please think of a number between {} and {}". format(low,high))

input ("Please ENTER to start ")

guesses = 1

while True :
    print ("\tGuessing in range of {}. to {}". format(low,high))
    guess = low + (high-low)//2
    print(guess)
    high_low = input ("My guess is {}. Should I guess higher or lower? "
                      "Enter h, l , or c if my guess is correct "
                      .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
         high = guess-1
    elif high_low == "c":
        print ("I got in {} guesses".format(guesses))
        exit()
    else:
        print ("Enter h, l or c")
    guesses = guesses+1