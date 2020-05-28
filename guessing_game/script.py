import random # import built-in functions as modules
# float('42')- convert int to float
# store number of guesses the player has made 
guesses_taken = 0

print("Hello! What is your name?")
my_name = input() # store the input in a variable
#random.randint()# function to generate random numbers
# randint() will return a random int between and incl between 1-20 the 2 int arguments passed
number = random.randint(1, 20)
# greet the user and explain purpose of program
print(f"Well, {my_name}, I am thinking of a number between 1 and 20")

# Execute and iterate through the the loop 6 times

for guesses_taken in range(6):
    # Guess the secret number and enter the guess
    print("Take a guess.")
    guess = input()
    # store the guess in a variable
    # input() value is a string so we conver into an int
    guess = int(guess)
# if user guess is less than random number
    if guess < number:
        print("Your guess is too low")
# if guess is greater than number
    elif guess > number:
        print("Your guess is too high")
# tells the exection to exit the loop
# if guess is right then stop the loop and go to next line
    elif guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print(f"Good job, {my_name}! You guessed my number in {guesses_taken} guesses!")

if guess != number:
    number = str(number)
    print(f"Nope! The number I was thinking of was {number}.")
