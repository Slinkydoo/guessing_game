import random
import time


class settings:
    def __init__(self, left_boundary, right_boundary, total_guesses, show_logic):
        settings.left_boundary = left_boundary
        settings.right_boundary = right_boundary
        settings.total_guesses = total_guesses
        settings.show_logic = show_logic


def settings_prompt(current_left_bound,  current_right_bound, current_total_guesses, current_show_logic):
    print("You can change the settings of the game here.")
    left_boundary = 1
    right_boundary = 100
    total_guesses = 10
    show_logic = False
    settings_confirmed = False
    print("The current settings are:\nLeft boundary =", current_left_bound, "\nRight boundary =", current_right_bound, "\nTotal guesses =", current_total_guesses,
          "\nShow logic =", current_show_logic)
    while not settings_confirmed:
        setting_input = input("Available settings:\n1) left boundary set\n2) right boundary set\n3) total guesses set"
                              "\n4) show logic\nEnter the number of the setting to change it or type c to confirm:\n")
        valid_setting_input = False
        if setting_input == "1":
            while not valid_setting_input:
                try:
                    print("Current boundary is", left_boundary)
                    left_boundary = int(input("What would you like the left boundary to be?\n"))
                    print("Left boundary has been set to", left_boundary)
                    print("Returning to settings menu.")
                    time.sleep(.5)
                    valid_setting_input = True
                except ValueError:
                    print("You must enter an integer.")
                    valid_setting_input = False
        elif setting_input == "2":
            while not valid_setting_input:
                try:
                    print("Current boundary is", right_boundary)
                    right_boundary = int(input("What would you like the right boundary to be?\n"))
                    print("Right boundary has been set to", right_boundary)
                    print("Returning to settings menu.")
                    time.sleep(.5)
                    valid_setting_input = True
                except ValueError:
                    print("You must enter an integer.")
                    valid_setting_input = False
        elif setting_input == "3":
            while not valid_setting_input:
                try:
                    print("Current number of guesses is", total_guesses)
                    total_guesses = int(input("How many total guesses would you like?\n"))
                    print("Total guesses have been set to", total_guesses)
                    print("Returning to settings menu.")
                    time.sleep(.5)
                    valid_setting_input = True
                except ValueError:
                    print("You must enter an integer.")
                    valid_setting_input = False
        elif setting_input == "4":
            while setting_input == "4" or setting_input.lower() != "y" or setting_input.lower() != "n":
                setting_input = input("Would you like to show the logic used by the "
                                      "computer each time you guess? (Y/N)\n")
                if setting_input.lower() == "y":
                    show_logic = True
                    print("Logic will be shown after each guess.")
                    print("Returning to settings menu.")
                    time.sleep(.5)
                elif setting_input.lower() == "n":
                    show_logic = False
                    print("Logic will NOT be shown after each guess.")
                    print("Returning to settings menu.")
                    time.sleep(.5)
        elif setting_input.lower() == "c":
            settings_confirmed = True
            return settings(left_boundary, right_boundary, total_guesses, show_logic)


current_settings = settings(1, 100, 10, False)

print("Welcome to the number guessing game.")
time.sleep(1)
print("In this game a random number will be generated between " + str(current_settings.left_boundary), "and",
      str(current_settings.right_boundary) + ".")
time.sleep(1)
print("The goal is to guess the number in less than " + str(current_settings.total_guesses), "tries.")
time.sleep(1)

settings_query = input("Would you like to change the settings? (Y/N)\n")
if settings_query.lower() == "y":
    current_settings = settings_prompt(current_settings.left_boundary, current_settings.right_boundary,
                                       current_settings.total_guesses, current_settings.show_logic)

guess = 0
number_guessed: bool = False
while guess != "n" and not number_guessed:
    random_number = random.choice(range(current_settings.left_boundary, current_settings.right_boundary, 1))
    print("Random number was selected. \nGood Luck!")
    guesses_left: int = current_settings.total_guesses
    previous_guess: int = -1
    past_count: int = 0
    guess = 0

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

        if valid_input:
            if guess == random_number:
                # This is the base case which will exit the loop once it reaches the end
                number_guessed = True
            elif (guess < current_settings.left_boundary or guess > current_settings.right_boundary) and guess != 0:
                # This runs if the guess is outside the boundaries given
                print("Guess must be between " + str(current_settings.left_boundary), "and",
                      str(current_settings.right_boundary) + ".")
            elif previous_guess == -1:
                # This runs for the first guess of each game
                if random_number - 5 <= guess <= random_number + 5:
                    print("Hot!!")
                elif random_number - 10 <= guess <= random_number + 10:
                    print("Warm.")
                elif random_number - 15 <= guess <= random_number + 15:
                    print("Cold.")
                else:
                    print("Freezing!!")

            # This section is for the subsequent guesses after the first
            elif guesses_left != 0:
                if previous_guess == guess:
                    print("That was your previous guess. Guess a different number")
                    guesses_left += 1
                # If the guess is BETWEEN the previous guess and the random number then you are warmer
                elif (previous_guess < guess < random_number) or (random_number < guess < previous_guess):
                    print("Warmer...")

                elif (previous_guess < guess and random_number < guess and previous_guess < random_number) or (
                        previous_guess > random_number and random_number > guess and previous_guess > random_number):
                    # This runs if the guess is greater than the previous guess AND the random number then you have
                    # gone too far, same is true with the inverse
                    if past_count == 0:
                        print("Warmer...but too far!! ")
                    else:
                        print("You passed the random number again!")
                    past_count += 1

                else:
                    print("Colder...")

            if not guesses_left == current_settings.total_guesses:
                previous_guess = guess

    if guess == "e":
        print("Game ended.")
    elif number_guessed:
        print("Congratulations! You guessed the number!")
    else:
        print("Sorry you ran out of tries. \nThe number was", random_number)
    guess = str(input("Would you like to play again? (y/n): "))
    number_guessed = False

print("Thanks for playing, Goodbye!")
