from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    print( " "+board[7]+" | "+board[8]+" "+"|"+" "+board[9]+" ")
    print( " "+board[4]+" | "+board[5]+" "+"|"+" "+board[6]+" ")
    print( " "+board[1]+" | "+board[2]+" "+"|"+" "+board[3]+" ")

def player_input():
    
    # Asking player 1 to choose X or O
    
    marker = input("Player 1 :Do you want to be 'X' OR 'O': ").upper()
    while marker!="X" and marker!="O":
          marker = input("Player 1 :Do you want to be 'X' OR 'O': ").upper()
    
    #Assigning the variable to player 1
    
    player1=marker
    
    if player1=='X':
        player2='O'
        
    
    elif player1=='O':
        player2='X'
    
    return (player1,player2)  

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    if board[7]==board[8]==board[9]==mark:
        return True
    elif board[4]==board[5]==board[6]==mark:
        return True
    elif board[1]==board[2]==board[3]==mark:
        return True
    elif board[7]==board[4]==board[1]==mark:
        return True
    elif board[8]==board[5]==board[2]==mark:
        return True
    elif board[9]==board[6]==board[3]==mark:
        return True
    elif board[7]==board[5]==board[3]==mark:
        return True
    elif board[9]==board[5]==board[1]==mark:
        return True
    else:
        return False


import random

def choose_first():
    
    
    var=random.randint(1,2)
    if var==1:
        print("Player 1 will go first")
        return int(0)
        
    else:
        print("Player 2 will go first")
        return int(1)

def space_check(board, position):
    return board[position]==" "

def full_board_check(board):
    space=0
    for item in board:
        if item==" ":
            space+=1
    return space==0        

def player_choice(board):
    mylist=[1,2,3,4,5,6,7,8,9]
    player_input=0
    while player_input not in [1,2,3,4,5,6,7,8,9] or not space_check(board, player_input):
        player_input= int(input("Choose your next position: (1-9): "))
    
    return player_input

def replay():
    player_wish= input("Do you want to play again? Enter YES or NO: ").upper()
    
    while player_wish!="YES" and player_wish!="NO":
        player_wish= input("Do you want to play again? Enter YES or NO: ").upper()
    if player_wish=="YES":
        return True
    elif player_wish=="NO":
        return False

print('Welcome to Tic Tac Toe!')

while True:
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    selected_input=player_input()
    selected_order= choose_first()
    count=selected_order
    ready = input('Are you ready to play? Enter Yes or No: ').upper()
    if ready[0]=="Y":
        game_on = True
    else: 
        game_on = False
    
    while game_on:
        if count%2==0:
            # player 1 turn
            
            place_marker(test_board,selected_input[0],player_choice(test_board))
            if win_check(test_board,selected_input[0]):
                display_board(test_board)
                print("Congratulation!! Player 1 has won the game!! ")
                game_on=False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('The game is draw')
                    game_on=False
                else:
                    display_board(test_board)
                    count+=1
                    
            
        else:   
            place_marker(test_board,selected_input[1],player_choice(test_board))
            if win_check(test_board,selected_input[1]):
                display_board(test_board)
                print("Congratulation!! Player 2 has won the game!! ")
                game_on=False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('The game is draw')
                    game_on=False
                else:
                    display_board(test_board)
                    count+=1
            
            
    if not replay():
        break
        
