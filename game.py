# ADD YOUR CODE BELOW

def main():
    # Prompt the user for the level
    level = int(input("Level: "))

    # Handle invalid input for the level (i.e., when level is below 1)
    while level < 1:
        print("Please enter a valid level above 0.")
        level = int(input("Level: "))

    # Determine the correct number to guess based on the level
    correct_number = level  # This means the answer will be the same as the level for now.

    # Now start the guessing loop
    while True:
        # Get the user's guess
        guess = input("Guess: ")

        # If the guess is not an integer, prompt again
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        # Convert the guess to an integer
        guess = int(guess)

        # Check the guess
        if guess < correct_number:
            print("Too small!")
        elif guess > correct_number:
            print("Too large!")
        else:
            print("Just right!")
            break  # Correct guess, exit the loop

if __name__ == "__main__":
    main()