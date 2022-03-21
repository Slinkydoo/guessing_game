import random
import time

hints = {
    "prev": "That was your previous guess. Guess a different number",
    "warm": "Warmer...",
    "cold": "Colder...",
    "too_far": "Warmer...but too far!",
    "too_far_again": "Too far again."
}
class settings:
    def __init__(self, left_boundary, right_boundary, total_guesses, show_logic):
        settings.left_boundary = left_boundary
        settings.right_boundary = right_boundary
        settings.total_guesses = total_guesses
        settings.show_logic = show_logic


def settings_prompt(current_left_bound,  current_right_bound, current_total_guesses, current_show_logic=False):
    print("You can change the settings of the game here.")
    # left_boundary = 1
    # right_boundary = 100
    # total_guesses = 10
    # show_logic = False
    settings_confirmed = False
    print("The current settings are:\n")
    time.sleep(.75)
    print("Left boundary =", current_left_bound, "\nRight boundary =", current_right_bound, "\nTotal guesses =", current_total_guesses,
          "\nShow logic =", current_show_logic, "\n")
    time.sleep(.75)
    while not settings_confirmed:
        setting_input = input("Available settings:\n1) left boundary set\n2) right boundary set\n3) total guesses set"
                              "\n4) show logic\nEnter the number of the setting to change it or type c to confirm:\n")
        valid_setting_input = False
        if setting_input == "1":
            while not valid_setting_input:
                print("Current left boundary is", current_left_bound)
                catch_left_bound = current_left_bound

                try:
                    current_left_bound = int(input("What would you like the left boundary to be?\n"))
                    valid_setting_input = True
                except ValueError:
                    print("You must enter an integer.")
                    valid_setting_input = False

                if current_left_bound > current_right_bound:
                    print("Left boundary must be less than", current_right_bound, "\nLeft boundary was not changed.")
                    time.sleep(1)
                    current_left_bound = catch_left_bound
                else:
                    print("Left boundary has been set to", current_left_bound)

                print("Returning to settings menu.")
                time.sleep(.75)

        elif setting_input == "2":
            while not valid_setting_input:
                print("Current right boundary is", current_right_bound)
                catch_right_bound = current_right_bound

                try:
                    current_right_bound = int(input("What would you like the right boundary to be?\n"))
                    valid_setting_input = True
                except ValueError:
                    print("You must enter an integer.")
                    valid_setting_input = False

                if current_right_bound < current_left_bound:
                    print("Right boundary must be greater than", current_left_bound, "\nRight boundary was not changed.")
                    time.sleep(1)
                    current_right_bound = catch_right_bound
                else:
                    print("Right boundary has been set to", current_right_bound)

                print("Returning to settings menu.")
                time.sleep(.75)

        elif setting_input == "3":
            while not valid_setting_input:
                try:
                    print("Current number of guesses is", current_total_guesses)
                    current_total_guesses = int(input("How many total guesses would you like?\n"))
                    print("Total guesses have been set to", current_total_guesses)
                    print("Returning to settings menu.")
                    time.sleep(.75)
                    valid_setting_input = True
                except ValueError:
                    print("You must enter an integer.")
                    valid_setting_input = False
        elif setting_input == "4":

            while setting_input == "4" or setting_input.lower() != "y" and setting_input.lower() != "n":

                if current_show_logic:
                    print("Current Settings reflect logic will be shown.")
                else:
                    print("Current settings reflect logic will NOT be shown.")

                setting_input = input("Would you like to show the logic used by the "
                                      "computer each time you guess? (Y/N)\n")

                if setting_input.lower() == "y":
                    current_show_logic = True
                    print("Logic will be shown after each guess.")
                    print("Returning to settings menu.")
                    time.sleep(.75)
                elif setting_input.lower() == "n":

                    current_show_logic = False
                    print("Logic will NOT be shown after each guess.")
                    print("Returning to settings menu.")
                    time.sleep(.75)
                else:
                    print("Input not understood. Please enter either \"y\" for yes or \"n\" for no.")
                    time.sleep(1.25)

        elif setting_input.lower() == "c":
            settings_confirmed = True
            return settings(current_left_bound, current_right_bound, current_total_guesses, current_show_logic)


current_settings = settings(1, 100, 10, False)

print("Welcome to the number guessing game.")
time.sleep(1)
print("In this game a random number will be generated between " + str(current_settings.left_boundary), "and",
      str(current_settings.right_boundary) + ".")
time.sleep(1)
print("The goal is to guess the number in less than " + str(current_settings.total_guesses), "tries.")
time.sleep(1)

settings_query = input("Would you like to change the settings? (y/n)\n")
if settings_query.lower() == "y":
    current_settings = settings_prompt(current_settings.left_boundary, current_settings.right_boundary,
                                       current_settings.total_guesses, current_settings.show_logic)

guess = 0
number_guessed: bool = False
while guess != "n" and not number_guessed:
    random_number = random.choice(range(current_settings.left_boundary, current_settings.right_boundary, 1))
    print("Random number was selected. \nGood Luck!")
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

            # The first guess of each game should tell the user how close they are to the random number
            elif previous_guess == current_settings.left_boundary - 1:
                if random_number - 5 <= guess <= random_number + 5:
                    print("Hot!!")
                elif random_number - 10 <= guess <= random_number + 10:
                    print("Warm.")
                elif random_number - 15 <= guess <= random_number + 15:
                    print("Cold.")
                else:
                    print("Freezing!!")

            # This section is for the subsequent guesses after the first
            elif guesses_left != 0 and not current_settings.show_logic:
                if previous_guess == guess:
                    print(hints["prev"])
                    # print("That was your previous guess. Guess a different number")
                    guesses_left += 1

                # If the guess is BETWEEN the previous guess and the random number then you are warmer
                elif (previous_guess < guess < random_number) or (random_number < guess < previous_guess):
                    print(hints["warm"])
                    # print("Warmer...")

                # If the guess is greater than the previous guess AND the random number then you went too far.
                # Also, if the guess is less than the previous guess AND the random number
                elif (previous_guess < guess and random_number < guess and previous_guess < random_number) or (
                        previous_guess > random_number and random_number > guess and previous_guess > random_number):
                    if past_count == 0:
                        print(hints["too_far"])
                        # print("Warmer...but too far!! ")
                    else:
                        print(hints["too_far_again"])
                        # print("You passed the random number again!")
                    past_count += 1

                else:
                    print(hints["cold"])
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
