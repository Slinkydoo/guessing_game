import helpers
import random
import time
print("Welcome to the number guessing game.")
time.sleep(1)
print("In this game a random number will be generated between 1 and 1000.")
time.sleep(1)
print("The goal is to guess the number in less than 10 tries.")
time.sleep(1)

guess = 0
number_guessed = False

while guess != "n" and not number_guessed:
    random_number = random.choice(range(1, 1000, 1))
    print("Random number was selected.")
    guesses_left = 10
    previous_guess = -1
    past_count = 0
    while not number_guessed and guesses_left != 0:
        try:
            guess = int(input("Enter your guess (" + str(guesses_left) + " guesses left): "))
            guesses_left -= 1
        except ValueError:
            print("You must enter an integer between 1 and 1000.")
            print("A guess has been used.")

        if guess == random_number:
            number_guessed = True
        # This section of the if is for the first guess
        elif (guess < 1 or guess > 1000) and guess != 0:
            print("Guess must be between 1 and 1000")
        elif previous_guess == -1:
            if guess > random_number - 50 and guess < random_number + 50:
                print("Hot!!")
            elif guess > random_number - 100 and guess < random_number + 100:
                print("Warm.")
            elif guess > random_number - 150 and guess < random_number + 150:
                print("Cold.")
            else:
                print("Freezing!!")

        # This section is for the subsequent guesses after the first
        else:
            # If the guess is BETWEEN the previous guess and the random number then you are warmer
            if (previous_guess < guess and guess < random_number) or (random_number < guess and guess < previous_guess):
                print("Warmer...")
            # If the guess is greater than the previous guess AND the random number then you have gone too far
            # same is true with the inverse
            elif (previous_guess < guess and random_number < guess) or (previous_guess > random_number and random_number > guess):
                if past_count == 0:
                    print("Woah too far!! ")
                else:
                    print("You passed the random number again!")
                past_count += 1

            else:
                print("Colder...")
        previous_guess = int(guess)


    if number_guessed == True:
        print("Congratulations! You guessed the number!")
    else:
        print("Sorry you ran out of tries.")
    guess = str(input("Would you like to play again? (y/n): "))
    number_guessed = False

print("Thanks for playing, Goodbye!")
