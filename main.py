import random
import time
from math import ceil, floor
import game_library

# Default Settings
current_settings = game_library.Settings(1, 100, 10, False)

print("Welcome to the number guessing game.")
time.sleep(1)
print("In this game a random number will be generated between " + str(current_settings.left_boundary), "and",
      str(current_settings.right_boundary) + ".")
time.sleep(1)
print("The goal is to guess the number in less than " + str(current_settings.total_guesses), "tries.")
time.sleep(1)

settings_query = input("Would you like to change the Settings? (y/n)\n")
if settings_query.lower() == "y":
    current_settings = game_library.settings_prompt(current_settings.left_boundary, current_settings.right_boundary,
                                       current_settings.total_guesses, current_settings.show_logic)

guess = 0
number_guessed: bool = False
while guess != "n" and not number_guessed:
    random_number = random.choice(range(current_settings.left_boundary, current_settings.right_boundary, 1))
    print("Random number was selected. \nGood Luck!")
    # The commented line below is for testing inputs
    # print("Random number is: ", random_number)
    guesses_left: int = current_settings.total_guesses
    previous_guess: int = current_settings.left_boundary - 1
    past_count: int = 0
    guess = 0

    # This loop runs the game constantly until the user guesses the number or runs out of guesses
    while not number_guessed and guesses_left != 0:

        # This try block will catch a Value error if the user inputs anything other than an integer
        try:
            guess = int(input("Enter your guess (" + str(guesses_left) + " total_guesses left): "))
            guesses_left -= 1
            valid_input = True
        except ValueError:
            print("You must enter an integer between " + str(current_settings.left_boundary), "and",
                  str(current_settings.right_boundary) + ".")
            valid_input = False

        # This if statement will only run if the input is valid which indirectly forces the user
        # to enter valid input or be in a continuous loop if they do not enter valid input
        if valid_input:

            # If the user guesses the number reflect this in a variable that will exit the game loop
            if guess == random_number:
                number_guessed = True

            # If the users guess is outside the boundaries then tell the user the guess must
            # be between the current boundaries but this should not use a guess
            elif (guess < current_settings.left_boundary or guess > current_settings.right_boundary) and guess != 0:
                # This runs if the guess is outside the boundaries given
                print("Guess must be between " + str(current_settings.left_boundary), "and",
                      str(current_settings.right_boundary) + ".")
                guesses_left += 1

            # The first guess of each game should tell the user how close they are to the random number based
            # on the difference of the boundaries
            elif previous_guess == current_settings.left_boundary - 1:

                if random_number - (floor(current_settings.right_boundary - current_settings.left_boundary) // 10) <= guess\
                        <= random_number + (ceil(current_settings.right_boundary - current_settings.left_boundary) // 10):
                    print("Hot!!")
                elif random_number - (floor(current_settings.right_boundary - current_settings.left_boundary) // 4) <= guess\
                        <= random_number + (ceil(current_settings.right_boundary - current_settings.left_boundary) // 4):
                    print("Warm.")
                elif random_number - (floor(current_settings.right_boundary - current_settings.left_boundary) // 2) <= guess\
                        <= random_number + (ceil(current_settings.right_boundary - current_settings.left_boundary) // 2):
                    print("Cold.")
                else:
                    print("Freezing!!")

            # This section is for the subsequent guesses after the first
            elif guesses_left != 0 and not current_settings.show_logic:
                if previous_guess == guess:
                    print(game_library.hints["prev"])
                    # print("That was your previous guess. Guess a different number")
                    guesses_left += 1

                # If the guess is BETWEEN the previous guess and the random number then you are warmer
                elif (previous_guess < guess < random_number) or (random_number < guess < previous_guess):
                    print(game_library.hints["warm"])
                    # print("Warmer...")

                # If the guess is greater than the previous guess AND the random number then you went too far.
                # Also, if the guess is less than the previous guess AND the random number
                elif (previous_guess < guess and random_number < guess and previous_guess < random_number) or (
                        previous_guess > random_number and random_number > guess and previous_guess > random_number):
                    if past_count == 0:
                        print(game_library.hints["too_far"])
                        # print("Warmer...but too far!! ")
                    else:
                        print(game_library.hints["too_far_again"])
                        # print("You passed the random number again!")
                    past_count += 1

                else:
                    print(game_library.hints["cold"])
                    # print("Colder...")

            if not guesses_left == current_settings.total_guesses:
                previous_guess = guess

    # If the user guessed the number, print a winning message then ask if they want to play again
    if guess == "e":
        print("Game ended.")
    elif number_guessed:
        print("Congratulations! You guessed the number!")
    else:
        print("Sorry you ran out of tries. \nThe number was", random_number)
    guess = str(input("Would you like to play again? (y/n): "))
    number_guessed = False

print("Thanks for playing, Goodbye!")
