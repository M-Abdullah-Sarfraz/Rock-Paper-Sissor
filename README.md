Rock Paper Scissors Game

This is a Python implementation of the classic Rock-Paper-Scissors game where a player competes against the computer system for 5 rounds. The game determines a winner based on the standard rules of Rock-Paper-Scissors:

Rock (✊) beats Scissors (✌)

Scissors (✌) beats Paper (✋)

Paper (✋) beats Rock (✊)



Features

User-friendly interaction for the player.

Randomized system choice for fair gameplay.

Automatic scoring for both the player and the system.

Declares the winner after 5 rounds.



How to Play

Run the Python script.

Enter your name when prompted.

Enter one of the symbols when prompted:

✊ for Rock

✋ for Paper

✌ for Scissors

The game will display the result of each round and update the scores.

After 5 rounds, the game announces the overall winner.



Prerequisites

Python 3.x must be installed on your system.



How to Run

Clone or download this repository.

Navigate to the directory containing the script.

Run the script using the command:

python3 rock_paper_scissors.py



Example Gameplay

Enter your name! John
Enter any symbol (✊, ✋ , ✌ ) ✊
John : wins
John choose ✊ and System choose ✌
John Score:  1 System Score :  0
...
System Win the Game


Rules

The player must enter only ✊, ✋, or ✌ as input. Any other input will be considered invalid.

Each round updates the score, and a winner is determined based on who has the highest score after 5 rounds.



Code Structure

rock(): Determines the outcome if the player chooses Rock.

scissor(): Determines the outcome if the player chooses Scissors.

paper(): Determines the outcome if the player chooses Paper.

The main logic handles the input and ensures the correct functions are called based on the player's choice.

Contributing

Feel free to fork this repository, make improvements, and submit a pull request. Contributions are welcome!

License

This project is licensed under the MIT License. Feel free to use and modify the code.
