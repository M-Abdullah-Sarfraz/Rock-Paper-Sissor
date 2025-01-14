import math, random

Player_Score = 0
Computer_Score = 0

# Function for rock input 
def rock():
    global Player_Score, Computer_Score 
    if Player == '✊' and computer_input == '✌':
        print(f"{name} : wins")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
        Player_Score = Player_Score +1
        
        
    elif Player == '✊' and computer_input == '✋':
        print(f"{name} : loose")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
        Computer_Score = Computer_Score +1
       
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
    
    print(f"{name} Score:  {Player_Score} Computer Score :  {Computer_Score}" )


# Function for scissor input 
def scissor():
    global Player_Score, Computer_Score 
    if Player == '✌' and computer_input == '✊':
        print(f"{name} : Loose")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
        Computer_Score = Computer_Score +1
        
    elif Player == '✌' and computer_input == '✋':
        print(f"{name} : Wins")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
        Player_Score = Player_Score +1
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )

    print(f"{name} Score:  {Player_Score} Computer Score :  {Computer_Score}" )

# Function for paper input 
def paper():
    global Player_Score, Computer_Score 
    if Player == '✋' and computer_input == '✊':
        print(f"{name} : wins")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
        Player_Score = Player_Score +1
       
    elif Player == '✋' and computer_input == '✌':
        print(f"{name} : loose")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
        Computer_Score = Computer_Score +1
     
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
    
    print(f"{name} Score:  {Player_Score} Computer Score :  {Computer_Score}" )


# Taking input from computer and Player
games_input = [ '✊', '✋' , '✌' ]
name = input("Enter your name! ")


# Rounds to play game
for i in range(0,5):
    Player = input("Enter any symbol (✊, ✋ , ✌ )")
    computer_input = random.choice(games_input)

    # Conditions with respect to player input 
    if Player == '✊':
        rock()
    elif Player == '✌':
        scissor()
    elif Player == '✋':
        paper()
    else:
     print("Wrong Input")

if Player_Score > Computer_Score:
    print(f"{name} Win the Game")
else:
    print("Computer  Win the Game")

    













