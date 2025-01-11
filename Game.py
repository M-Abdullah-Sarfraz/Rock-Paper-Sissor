import math, random

# Function for rock input 
def rock():
    
    if Player == '✊' and computer_input == '✌':
        print(f"{name} : wins")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
        
    elif Player == '✊' and computer_input == '✋':
        print(f"{name} : loose")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )


# Function for scissor input 
def scissor():
    if Player == '✌' and computer_input == '✊':
        print(f"{name} : wins")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
    elif Player == '✌' and computer_input == '✋':
        print(f"{name} : loose")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )



# Function for paper input 
def paper():
    if Player == '✋' and computer_input == '✊':
        print(f"{name} : wins")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
    elif Player == '✋' and computer_input == '✌':
        print(f"{name} : loose")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and computer choose {computer_input}" )


# Taking input from computer and Player

games_input = [ '✊', '✋' , '✌' ]
name = input("Enter your name! ")
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


