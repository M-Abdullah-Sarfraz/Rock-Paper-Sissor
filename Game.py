import math, random

games_input = [ '✊', '✋' , '✌' ]


player1 = ""
computer_input = str(random.choice(games_input))
print(computer_input)

def rock():
    player1 = str(input("Enter any symbol (✊, ✋ , ✌ )"))
    if player1 == '✊' or computer_input == '✌':
        print("Player 1 wins")
        print("Player 1 choose "+ player1 + "Computer choose " + computer_input)
    elif player1 == '✊' or computer_input == '✋':
        print("Player 1 loose")
        print("Player 1 choose "+ player1 + "Computer choose " + computer_input)
    # else:
    #     print("GAME DRAW")
    #     print("Player 1 choose "+ player1 + "Computer choose " + computer_input)

 
rock()
