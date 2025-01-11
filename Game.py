import math, random


# Function for rock input 
def rock():
    global Player_Score, System_Score 
    if Player == '✊' and System_input == '✌':
        print(f"{name} : wins")
        print(f"{name} choose  {Player}  and System choose {System_input}" )
        Player_Score = Player_Score +1
        
        
    elif Player == '✊' and System_input == '✋':
        print(f"{name} : loose")
        print(f"{name} choose  {Player}  and System choose {System_input}" )
        System_Score = System_Score +1
       
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and System choose {System_input}" )
    
    print(f"{name} Score:  {Player_Score} System Score :  {System_Score}" )


# Function for scissor input 
def scissor():
    global Player_Score, System_Score 
    if Player == '✌' and System_input == '✊':
        print(f"{name} : wins")
        print(f"{name} choose  {Player}  and System choose {System_input}" )
        Player_Score = Player_Score +1
    elif Player == '✌' and System_input == '✋':
        print(f"{name} : loose")
        print(f"{name} choose  {Player}  and System choose {System_input}" )
        System_Score = System_Score +1
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and System choose {System_input}" )

    print(f"{name} Score:  {Player_Score} System Score :  {System_Score}" )

# Function for paper input 
def paper():
    global Player_Score, System_Score 
    if Player == '✋' and System_input == '✊':
        print(f"{name} : wins")
        print(f"{name} choose  {Player}  and System choose {System_input}" )
        Player_Score = Player_Score +1
       
    elif Player == '✋' and System_input == '✌':
        print(f"{name} : loose")
        print(f"{name} choose  {Player}  and System choose {System_input}" )
        System_Score = System_Score +1
     
    else:
        print("GAME DRAW")
        print(f"{name} choose  {Player}  and System choose {System_input}" )
    
    print(f"{name} Score:  {Player_Score} System Score :  {System_Score}" )


# Taking input from System and Player
games_input = [ '✊', '✋' , '✌' ]
name = input("Enter your name! ")

#Initial Scores
Player_Score = 0
System_Score = 0

# Rounds to play game
for i in range(0,5):
    Player = input("Enter any symbol (✊, ✋ , ✌ )")
    System_input = random.choice(games_input)

    # Conditions with respect to player input 
    if Player == '✊':
        rock()
    elif Player == '✌':
        scissor()
    elif Player == '✋':
        paper()
    else:
     print("Wrong Input")


#Game Winner
if Player_Score > System_Score:
    print(f"{name} Win the Game")
else:
    print("System  Win the Game")

    













