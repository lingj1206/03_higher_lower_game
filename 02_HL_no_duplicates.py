SECRET = 7
GUESSES_ALLOWED = 5
already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))

    if guess in already_guessed:
        print("You already guessed that number!  Please try a different number")
        print(f"You still have {guesses_left} guesses left")

        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print(f"Too low, try a higher number. Guesses left: {guesses_left}")

        elif guess > SECRET:
            print(f"Too high, try a lower number. Guesses left: {guesses_left}")

    else:
        if guess < SECRET:
            print("Too low")
        elif guess < SECRET:
            print("Too high")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED:
        print("Congratulations, you got the secret number")
