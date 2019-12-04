# Magic Number Game

## Firstly it is important to import the neccessary libraries, in this instance we use the 'random' library
## so we can use the random.randint statement to generate a random number
import random

## This assignment here takes into account the number of guesses the user has had
## and intially sets it to 0.

guessuesTaken = 0

## the print function here asks the user for their name
## while the 'user_name_input' ask for a prompt from the user
print("Hello!, what is you name?")
user_name_input = str(input())

## generate the random number, we can use the keyword 'breakpoint()' to debug our code and inspect our variables. and stop our code at a specific point in time
## after getting the responce of the name of the user, the code generates a random number
## it can then proceede to the next print command, where it asks the user for an integer input.

number = random.randint(1,10)
print("Well" + " " +user_name_input +" "+"I am thinking of a number between 1 - 20")

## This 'while' loop will be explained step by step:
    ## so if we think like a computer and try to explain it in pseudocode, the block of code has recognised that
    ## guessesTaken is below 10, so prints the intial "take a guess" as it was set at 0 prior to the loop.
    ## and in the while loop we can see that guessesTaken increases through every iteration by 1.
while guessuesTaken < 10:
    print("Take a guess!")
    guess = int(input("Your Guess"))

    guessuesTaken = guessuesTaken + 1

    ## here the if statements are quite clear, if the guess variable is lower, higher or equal to the number it prints the appropriate responce.
    if guess < number:
        print("Not quite, you were under the value")

    if guess > number:
        print("Not quite, your guess is over the value")
    ## this step is CRUCIAL to stop the loop, which is impleneting the 'break' keyword after the conditon has been successfully met.
    if guess == number:
        break
if guess == number:
    guessuesTaken = str(guessuesTaken)
    print("Good job" + " " + user_name_input + " " + "you guessed it in" + " " + guessuesTaken + " " + "guess(es)")

if guess != number:
    number = str(number)
    print("Nope. I was thinking of" + number)
