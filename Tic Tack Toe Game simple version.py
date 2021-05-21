#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']


# In[3]:


def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3]+'|')
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6]+'|')
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9]+'|')


# In[4]:


display_board(test_board)


# In[5]:


def player_input():
    
    marker = "wrong"
    
    while marker not in ['X','O']:
        
        marker = input("Player1: Please choose your valueas 'X' or 'O': ")
        
        if marker not in ['X','O']:
            clear_output()
            print("Incorrect Value ! Please Choose X or O")
            
    player1 = marker
    
    if player1 == 'X':
        player2= 'O'
    else:
        player2 = 'X'
            
            
    return (player1,player2)


# In[6]:


player_marker_1,player_marker_2 = player_input()


# In[7]:


player_marker_2


# In[8]:


def place_marker(board, marker, position):
    board[position] = marker


# In[9]:


place_marker(test_board,'$',7)
display_board(test_board)


# In[10]:


def win_check(board, mark):
    if board[1]==board[2]==board[3]== mark:
        return True
    elif board[4]==board[5]==board[6]== mark:
        return True
    elif board[7]==board[8]==board[9]== mark:
        return True
    elif board[1]==board[4]==board[7]== mark:
        return True
    elif board[2]==board[5]==board[8]== mark:
        return True
    elif board[3]==board[6]==board[9]== mark:
        return True
    elif board[1]==board[5]==board[9]== mark:
        return True
    elif board[3]==board[5]==board[7]== mark:
        return True
    else:
        return False
    


# In[11]:


win_check(test_board,'X')


# In[12]:


import random

def choose_first():
    shuffle = random.randint(0,1)
    
    if shuffle == 0:
        return ("Player 1 ")
    else:
        return ("Player 2 ")


# In[13]:


choose_first()


# In[14]:


def space_check(board, position):
    return board[position] == ' '


# In[15]:


space_check(test_board,7)


# #Other way  
# def full_board_check(board):
#     for i in range(1,10):
#         if space_check(board,i):
#             return False
#         else:
#             return True

# In[16]:



def full_board_check(board):
    if board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] and board[9] == 'X':
        return True
    elif board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] and board[9] == 'O':
        return True
    else:
        return False


# In[17]:


full_board_check(test_board)


# In[18]:


def player_choice(board):
    
    position = "wrong"
    
    while position not in range(1,10) or space_check(board,position):
        position = int(input("Choose your position (1-9)"))
        
    return position
        


# In[19]:


player_choice(test_board)


# In[20]:


def replay():
    
    again = "again"
    
    while again not in ['Y','N']:
        
        again = input("Do You Wish To Play Again (Y or N) ? ")
        
        if again not in ['Y','N']:
            clear_output()
            print("Choose Y or N")
    if again == "Y":
        return True
    else:
        return False


# In[21]:


replay()


# In[22]:


print('Welcome to Tic Tac Toe!')

while True:
    
    board = ['']*10
    player_marker_1, player_marker_2 = player_input()
    
    
    turn = choose_first()
    print(turn+"will play First")
    
    
    play_game = input('Ready To Play ? Y or N')
    if play_game == 'Y':
            game_on = True
    else:
        game_on = False
        
        
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(board)
            
            position = player_choice(board)
            
            place_marker(board , player_marker_1 , position)
            
            if win_check(board, player_marker_1):
                display_board(board)
                print("PLAYER 1 HAS WON!!")
                game_on = False
                
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!!")
                    game_on = False
                else:
                    turn = 'Player 2'
                    
        else:
            display_board(board)
            
            position = player_choice(board)
            
            place_marker(board , player_marker_2 , position)
            
            if win_check(board, player_marker_2):
                display_board(board)
                print("PLAYER 2 HAS WON!!")
                game_on = False
                
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!!")
                    game_on = False
                else:
                    turn = 'Player 1'
            
        
    
    
    if not replay():
        break


# In[ ]:




