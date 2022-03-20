import random
import time

left_boundary = 1
right_boundary = 100
total_guesses = 10
print("Welcome to the number guessing game.")
time.sleep(1)
print("In this game a random number will be generated between " + str(left_boundary), "and", str(right_boundary) + ".")
time.sleep(1)
print("The goal is to guess the number in less than " + str(total_guesses), "tries.")
time.sleep(1)

guess = 0
number_guessed = False

while guess != "n" and not number_guessed:
    random_number = random.choice(range(left_boundary, right_boundary, 1))
    print("Random number was selected. \nGood Luck!")
    guesses_left = total_guesses
    previous_guess = -1
    past_count = 0
    guess = 0

    while not number_guessed and guesses_left != 0:
        # This try block will catch a Value error if the user inputs anything other than a integer
        try:
            guess = int(input("Enter your guess (" + str(guesses_left) + " total_guesses left): "))
            guesses_left -= 1
            valid_input = True
        except ValueError:
            print("You must enter an integer between " + str(left_boundary), "and", str(right_boundary) + ".")
            valid_input = False

        if valid_input:
            if guess == random_number:
                # This is the base case which will exit the loop once it reaches the end
                number_guessed = True
            elif (guess < left_boundary or guess > right_boundary) and guess != 0:
                # This runs if the guess is outside the boundaries given
                print("Guess must be between " + str(left_boundary), "and", str(right_boundary) + ".")
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

            if not guesses_left == total_guesses:
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
