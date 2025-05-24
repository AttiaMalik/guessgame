import random   #improt random for generate random number
secert_number = random.randint(1,100)

attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")    # show greeting message
print("Guess the number between 1 and 100.")

while attempts < max_attempts:       #loop for multiply attempts
    try:
        guess = int(input(f"attempts {attempts + 1}: "))

        if guess == secert_number:
            print("Congratulations! You guessed the correct number.")
        elif guess > secert_number:
            print("Too high")
        else:
            print("Too low")
        attempts += 1
    except ValueError:
        print("Please enter a valid number.")
if attempts == max_attempts and guess != secert_number:      #if user fail after max attempts
    print(f"Game Over! The correct number was: {secert_number}") 