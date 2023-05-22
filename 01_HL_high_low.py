# HL component 1 - Get (and check) user input

# number checking function
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None:
        situation = "low only"

    while True:
        try:
            response = int(input(question))

            # checks input is not too high or too low
            # if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}")
                    continue

            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more than (oe equal to) {low}")
                    continue

            return response

        except ValueError:
            print("Please enter an integer")
            continue


# main routine
lowest = int_check("Low number: ")
highest = int_check("High number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)
