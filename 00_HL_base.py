import random


# HL component 1 - Get (and check) user input
# number checking function
def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too hig etc)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


def check_rounds():
    while True:
        print("press <enter> to play infinite mode")
        response = input("How many rounds: ")

        round_error = "please press <enter>" \
                      "  or an integer that is more than 0"

        if response == "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
                else:
                    return response

            except ValueError:
                print(round_error)
                continue
        return response


def instructions():
    print("Welcome to the Higher Lower Game")
    print("You will be asked to enter a 'low' number and a 'high' number")
    print("The computer will generate a 'secret' number between your two chosen numbers")
    print("It will use the numbers for all the rounds in a given game")
    print("The computer will calculate how many guesses you are allowed")
    print("Enter the number of rounds you want to play")
    print("guess the secret number")
    print()
    return ""


def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# main routine
played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()

rounds_played = 0
rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5

end_game = "no"
while end_game == "no":

    lowest = int_check("Low number: ")
    highest = int_check("High number: ", lowest + 1)
    print()
    if mode == "infinite":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        rounds += 1
        print(heading)
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        print(heading)
    user_choice = int_check("")

    if rounds_played == rounds - 1:
        end_game = "yes"
    print()

    rounds_played += 1
    if user_choice == "xxx":
        break

    if rounds_played >= rounds:
        break
