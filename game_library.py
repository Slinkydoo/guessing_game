import time


hints = {
    "prev": "That was your previous guess. Guess a different number",
    "warm": "Warmer...",
    "cold": "Colder...",
    "too_far": "Warmer...but too far!",
    "too_far_again": "Too far again."
}


class Settings:
    def __init__(self, left_boundary, right_boundary, total_guesses, show_logic):
        Settings.left_boundary = left_boundary
        Settings.right_boundary = right_boundary
        Settings.total_guesses = total_guesses
        Settings.show_logic = show_logic


def check_valid_input(input_as_str, data_type):
    if data_type == "int":
        try:
            int(input_as_str)
            return True
        except ValueError:
            print("You must enter an integer.")
            return False
    elif data_type == "pos_int":
        try:
            int(input_as_str)
            return True
        except ValueError:
            print("You must enter a positive integer.")
            return False


def change_left_boundary(left_boundary: int, right_boundary: int, valid_boundaries=True):
    # This function assumes the input is invalid
    valid_setting_input = False

    if not valid_boundaries:
        print("The current boundaries are not valid")
        print("Please change the left boundary to be less than", str(right_boundary) + ".")
    while not valid_setting_input:
        left_boundary = input("What would you like the left boundary to be?\n")
        valid_setting_input = check_valid_input(left_boundary, "int")
        if valid_setting_input:
            left_boundary = int(left_boundary)
            if left_boundary < right_boundary:
                print("Left boundary has been set to", left_boundary)
    return left_boundary


def change_right_boundary(right_boundary: int, left_boundary: int, valid_boundaries=True):
    valid_setting_input = False
    if not valid_boundaries:
        print("The current boundaries are not valid")
        print("Please change the right boundary to be greater than", str(left_boundary) + ".")
    while not valid_setting_input:
        right_boundary = input("What would you like the right boundary to be?\n")
        valid_setting_input = check_valid_input(right_boundary, "int")
        if valid_setting_input:
            right_boundary = int(right_boundary)
            if left_boundary < right_boundary:
                print("Right boundary has been set to", right_boundary)
    return right_boundary


def settings_prompt(current_left_bound: int, current_right_bound: int, current_total_guesses: int,
                    current_show_logic=False):
    print("You can change the Settings of the game here.")
    settings_confirmed = False

    time.sleep(.75)
    while not settings_confirmed:
        print("The current Settings are:")
        time.sleep(.75)
        print("Left boundary =", current_left_bound, "\nRight boundary =", current_right_bound, "\nTotal guesses =",
              current_total_guesses,
              "\nShow logic =", current_show_logic, "\n")
        setting_input = input("Available Settings:\n1) left boundary set\n2) right boundary set\n3) total guesses set"
                              "\n4) show logic\nEnter the number of the setting to change it or type c to confirm:\n")
        valid_setting_input = False

        # Left boundary setting
        if setting_input == "1":
            current_left_bound = change_left_boundary(current_left_bound, current_right_bound)
            # The following loop will run if the user inputs invalid boundaries
            while current_left_bound >= current_right_bound:
                current_right_bound = change_right_boundary(current_right_bound, current_left_bound, False)
            print("Returning to Settings menu.")
            time.sleep(.75)

        # Right boundary setting
        elif setting_input == "2":
            current_right_bound = change_right_boundary(current_right_bound, current_left_bound)
            # The following loop will run if the user inputs invalid boundaries
            while current_right_bound <= current_left_bound:
                current_left_bound = change_left_boundary(current_left_bound, current_right_bound, False)
            print("Returning to Settings menu.")
            time.sleep(.75)

        # Total guesses setting
        elif setting_input == "3":
            while not valid_setting_input:
                print("Current number of guesses is", current_total_guesses)
                current_total_guesses = input("How many total guesses would you like?\n")
                valid_setting_input = check_valid_input(current_total_guesses, "int")
                if valid_setting_input:
                    current_total_guesses = int(current_total_guesses)
                    print("Total guesses have been set to", current_total_guesses)
                    print("Returning to Settings menu.")
                    time.sleep(.75)
                # try:
                #     current_total_guesses = int(input("How many total guesses would you like?\n"))
                #     print("Total guesses have been set to", current_total_guesses)
                #     print("Returning to Settings menu.")
                #     time.sleep(.75)
                #     valid_setting_input = True
                # except ValueError:
                #     print("You must enter an integer.")
                #     valid_setting_input = False

        # Show logic setting
        elif setting_input == "4":
            while setting_input == "4" or setting_input.lower() != "y" and setting_input.lower() != "n":

                if current_show_logic:
                    print("Current Settings reflect logic will be shown.")
                else:
                    print("Current Settings reflect logic will NOT be shown.")

                setting_input = input("Would you like to show the logic used by the "
                                      "computer each time you guess? (Y/N)\n")

                if setting_input.lower() == "y":
                    current_show_logic = True
                    print("Logic will be shown after each guess.")
                    print("Returning to Settings menu.")
                    time.sleep(.75)
                elif setting_input.lower() == "n":

                    current_show_logic = False
                    print("Logic will NOT be shown after each guess.")
                    print("Returning to Settings menu.")
                    time.sleep(.75)
                else:
                    print("Input not understood. Please enter either \"y\" for yes or \"n\" for no.")
                    time.sleep(1.25)

        elif setting_input.lower() == "c":
            settings_confirmed = True
            return Settings(current_left_bound, current_right_bound, current_total_guesses, current_show_logic)