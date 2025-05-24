
========================================
    Number Guessing Game (Python)
========================================

Description:
This is a simple command-line Number Guessing Game written in Python. 
The program randomly generates a number between 1 and 100. 
The player has to guess the correct number within a limited number of attempts (default: 5).

----------------------------------------

Features:
- Random number generation using Python's `random` module.
- Accepts user input and checks against the generated number.
- Provides hints: "Too high" or "Too low".
- Allows up to 5 attempts to guess the correct number.
- Displays success or failure messages appropriately.
- Handles invalid inputs gracefully using try-except.

----------------------------------------

How It Works:
1. The game starts with a welcome message.
2. A secret number is generated between 1 and 100.
3. The player is prompted to guess the number up to 5 times.
4. After each guess, the program tells the player if the guess was too high or too low.
5. If the guess is correct, a success message is displayed and the game ends.
6. If the maximum number of attempts is reached without a correct guess, the correct number is revealed.
7. If the user enters a non-numeric value, an error message is shown and the attempt is not counted.

----------------------------------------

Requirements:
- Python 3.x installed.
- No external libraries required (only uses the built-in `random` module).

----------------------------------------

How to Run:
1. Save the Python code in a file, for example: `guess_game.py`
2. Open a terminal or command prompt.
3. Navigate to the folder where the file is saved.
4. Run the script using the command:
   python guess_game.py

----------------------------------------

Sample Output:
Welcome to the Number Guessing Game!
Guess the number between 1 and 100.
Attempt 1: 50
Too low
Attempt 2: 75
Too high
Attempt 3: 68
Congratulations! You guessed the correct number.

----------------------------------------

Author:
Attia Malik

