def display_grid(gridList): #displays the Tic-Tac-Toe board
    
    for i in gridList:
        print("\t" * 6, "  |   |   ")
        print("\t" * 6, f"{i[0]} | {i[1]} | {i[2]}")
        print("\t" * 6, "  |   |   ")
        if i == [7, 8, 9]:
            print(' ')
        else:
            print("\t" * 6, '-' * 9)

def player_letter():     #assigned letter X or O to player 1 and player 2
    
    player1 = input("Player 1, Which letter do you choose: X or O? ").upper()
    player2 = 0
    
    while player1 not in ["X", "O"]:
        
        player1 = input("Sorry, need an X or an O. Try again.").upper()
    
    if player1 == "X":
        player2 = "O"
        print("Player 1 chose X, so Player 2 is an O!")
    else:
        player2 = "X"
        print("Player 1 chose O, therefore Player 2 is an X!")
        
    return player1, player2

def reset():   #asks for a replay of the game and resets the game board back to original numbers
    
    global grid_num_l, player1, player2, game_active 
    
    while True: 
    
        ask = input("Do you want to play again? Y or N? ").upper()

        if ask == 'Y':

            player1, player2 = player_letter()

            grid_num_l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

            display_grid(grid_num_l)
            
            break

        elif ask not in ['Y', 'N']:
            print('Need a y for yes or n for no: ') 
            

        else:
            grid_num_l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            game_active = False 
            break
        
    
    return game_active
    
def game_winner(triple, x):
    
    global player1, player2, game_active

    if (triple in grid_num_l) or triple in [[grid_num_l[0][0], grid_num_l[1][0], grid_num_l[2][0]],  
                                  [grid_num_l[0][1], grid_num_l[1][1], grid_num_l[2][1]],
                                  [grid_num_l[0][2], grid_num_l[1][2], grid_num_l[2][2]],
                                  [grid_num_l[0][0], grid_num_l[1][1], grid_num_l[2][2]],
                                  [grid_num_l[0][2], grid_num_l[1][1], grid_num_l[2][0]]]:
        
        if player1 == x:
            print("Player 1 Wins!")

        else:
            print("Player 2 Wins!")

        return reset()
            
def draw():
    
    global grid_num_l
    
    count = 0
    for i in grid_num_l:
        for j in i:
            if type(j) == str:
                count += 1

    if count == 9:
        print("It is a draw!")
        count = 0 #resets the count to 0 to use draw() again
        return reset()

    return count

def player_move(r, c, position, move, letter):
    
    if move == position:
        
        if type(grid_num_l[r][c]) == str:
            move = int(input("Already occupied. Try another position. "))
            
        else:
            grid_num_l[r][c] = letter
            display_grid(grid_num_l)

def player_input(player, letter, player_num):
    
    move = input(f"Player {player_num}, which position do you choose? ")
    
    while move not in str(list(range(1,10))) or move == "":
        move = input("Need an integer from 1 to 9. Try again. ")
    else:
        move = int(move)
    
    if player == letter:

        player_move(0, 0, 1, move, letter)

        player_move(0, 1, 2, move, letter)

        player_move(0, 2, 3, move, letter)

        player_move(1, 0, 4, move, letter)

        player_move(1, 1, 5, move, letter)

        player_move(1, 2, 6, move, letter)

        player_move(2, 0, 7, move, letter)

        player_move(2, 1, 8, move, letter)

        player_move(2, 2, 9, move, letter)

grid_num_l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #list contain numbers representing grid positions

player1, player2 = player_letter() #assigns players to their respective letter: X or O. 

game_active = True

def main():
    
    global grid_num_l

    display_grid(grid_num_l)
    
    game_winner(['X', 'X', 'X'], 'X')
    game_winner(['O', 'O', 'O'], 'O')

    
    while game_active:
        
        if player1 == 'X':

            player_input(player1, 'X', 1)
            p1_X_win = game_winner(['X', 'X', 'X'], 'X')
            
            if p1_X_win == False:
                break
                
            else:
                draw()
            
        else:
            
            player_input(player1, 'O', 1)
            p1_O_win = game_winner(['O', 'O', 'O'], 'O')
            
            if p1_O_win == False:
                break
                
            else:
                draw()
            
            
        if player2 == 'O':
                
            player_input(player2, 'O', 2)
            p2_O_win = game_winner(['O', 'O', 'O'], 'O')
            
            if p2_O_win == False:
                break
                
            else:
                draw()
        
        else:
            
            player_input(player2, 'X', 2)
            p2_X_win = game_winner(['X', 'X', 'X'], 'X')
            
            if p2_X_win == False:
                break
                
            else:
                draw()
                
                

main()


            


        