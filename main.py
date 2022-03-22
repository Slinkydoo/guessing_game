import random
import time
from math import ceil, floor
import game_library

# Default Settings
current_settings = game_library.Settings(1, 100, 10, False)
settings_confirmed = False
print("Welcome to the number guessing game.")
time.sleep(1)

# "Settings" loop -------------------------------------------------------------------------------------------------
while not settings_confirmed:
    print("In this game a random number will be generated between " + str(current_settings.left_boundary), "and",
          str(current_settings.right_boundary) + ".")
    time.sleep(1)
    print("The goal is to guess the number in less than " + str(current_settings.total_guesses), "tries.")
    time.sleep(1)

    settings_query = input("Would you like to change the settings? (y/n)\n")
    if settings_query.lower() == "y":
        current_settings = game_library.settings_prompt(current_settings.left_boundary, current_settings.right_boundary,
                                                            current_settings.total_guesses, current_settings.show_logic)
    settings_confirmed = True

    if settings_confirmed:
        guess = 0
        number_guessed: bool = False

        # "Game" loop ---------------------------------------------------------------------------------------------
        while guess != "n" and not number_guessed:
            random_number = random.choice(range(current_settings.left_boundary, current_settings.right_boundary, 1))
            print("Random number was selected. \nGood Luck!")
            # The commented line below is for testing inputs
            print("Random number is: ", random_number)
            start_time = time.time()
            guesses_left: int = current_settings.total_guesses
            previous_guess: int = current_settings.left_boundary - 1
            past_count: int = 0
            guess = 0
            show_logic_boundaries = [current_settings.left_boundary, current_settings.right_boundary]

            while not number_guessed and guesses_left != 0:
                # Checks for valid input
                guess = input("Enter your guess (" + str(guesses_left) + " guesses left): ")

                # This statement will allow the user to exit the game at any time
                if guess == "e":
                    break

                valid_input = game_library.check_valid_input(guess, "int")

                # This if statement will only run if the input is valid which indirectly forces the user
                # to enter valid input or be in a continuous loop if they do not enter valid input
                if valid_input:
                    guesses_left -= 1
                    guess = int(guess)
                    # If the user guesses the number reflect this in a variable that will exit the game loop
                    if guess == random_number:
                        number_guessed = True

                    # If the users guess is outside the boundaries then tell the user the guess must
                    # be between the current boundaries but this should not use a guess
                    elif guess < current_settings.left_boundary or guess > current_settings.right_boundary:
                        # This runs if the guess is outside the boundaries given
                        print("Guess must be between " + str(current_settings.left_boundary), "and",
                              str(current_settings.right_boundary) + ".")
                        guesses_left += 1

                    # The first guess of each game should tell the user how close they are to the random number based
                    # on the difference of the boundaries
                    elif previous_guess == current_settings.left_boundary - 1:

                        if random_number - (floor(current_settings.right_boundary - current_settings.left_boundary + 1) // 10)\
                                <= guess <=\
                                random_number + (ceil(current_settings.right_boundary - current_settings.left_boundary + 1) // 10):
                            print("Hot!!")
                            if current_settings.show_logic:
                                print("The random number is very close to", guess)

                        elif random_number - (floor(current_settings.right_boundary - current_settings.left_boundary+ 1) // 4)\
                                <= guess <=\
                                random_number + (ceil(current_settings.right_boundary - current_settings.left_boundary + 1) // 4):
                            print("Warm.")
                            if current_settings.show_logic:
                                print("The random number is close to", guess)

                        elif random_number - (floor(current_settings.right_boundary - current_settings.left_boundary + 1) // 2)\
                                <= guess <=\
                                random_number + (ceil(current_settings.right_boundary - current_settings.left_boundary + 1) // 2):
                            print("Cold.")
                            if current_settings.show_logic:
                                print("The random number is far from", guess)

                        else:
                            print("Freezing!!")
                            if current_settings.show_logic:
                                print("The random number is very far from", guess)

                    # This section is for the subsequent guesses after the first
                    elif guesses_left != 0:
                        if previous_guess == guess:
                            print(game_library.hints["prev"])
                            guesses_left += 1

                        # If the guess is BETWEEN the previous guess and the random number then you are warmer
                        elif (previous_guess < guess < random_number) or (random_number < guess < previous_guess):
                            print(game_library.hints["warmer"])
                            if current_settings.show_logic:
                                show_logic_boundaries = game_library.show_logic(show_logic_boundaries[0], show_logic_boundaries[1], guess, previous_guess, "warmer", random_number)
                                print('The random number must be between or equal to', show_logic_boundaries[0], "and", show_logic_boundaries[1])

                        # If the guess is greater than the previous guess AND the random number then you went too far.
                        # Also, if the guess is less than the previous guess AND the random number
                        elif (previous_guess < guess and random_number < guess and previous_guess < random_number)\
                                or (previous_guess > random_number and random_number > guess and previous_guess > random_number):
                            if past_count == 0:
                                print(game_library.hints["too_far"])
                            else:
                                print(game_library.hints["too_far_again"])
                            past_count += 1

                            if current_settings.show_logic:
                                show_logic_boundaries = game_library.show_logic(show_logic_boundaries[0], show_logic_boundaries[1],
                                                                                guess, previous_guess, "too_far",
                                                                                random_number)
                                print('The random number must be between or equal to', show_logic_boundaries[0], "and",
                                      show_logic_boundaries[1])

                        else:
                            print(game_library.hints["colder"])
                            if current_settings.show_logic:
                                show_logic_boundaries = game_library.show_logic(show_logic_boundaries[0], show_logic_boundaries[1],
                                                                                guess, previous_guess, "colder",
                                                                                random_number)
                                print('The random number must be between or equal to', show_logic_boundaries[0], "and",
                                      show_logic_boundaries[1])

                    if not guesses_left == current_settings.total_guesses and current_settings.left_boundary < guess < current_settings.right_boundary:
                        previous_guess = guess

            end_time = time.time()

            # If the user guessed the number, print a winning message then ask if they want to play again
            if end_time - start_time > 60:
                print("The game lasted", int(end_time - start_time) // 60, "minutes and", int(end_time - start_time) % 60, "seconds.")
            else:
                print("The game lasted", int(end_time - start_time), "seconds.")
            if guess == "e":
                print("Game ended.")
            elif number_guessed:
                print("Congratulations! You guessed the number in", (current_settings.total_guesses - guesses_left), "tries!")
            else:
                print("Sorry you ran out of tries. \nThe number was", random_number)
            guess = str(input("Would you like to play again? (y/n): "))
            # The following if statement will exit the "game" loop and return to the "settings" loop
            if guess == "y":
                settings_confirmed = False
                # guesses_left = 0

print("Thanks for playing, Goodbye!")
