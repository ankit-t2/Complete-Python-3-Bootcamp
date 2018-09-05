from IPython.display import clear_output
import os

my_board = ['#','X','O','X','X','X','O','O','O','X']

def draw_board(board):
    
    clear_output()
    print('   |   |   ')
    print(' {} | {} | {} '.format(board[7],board[8],board[9]))
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' {} | {} | {} '.format(board[4],board[5],board[6]))
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' {} | {} | {} '.format(board[1],board[2],board[3]))
    print('   |   |   ')
    
def get_user_choice():
    
    valid_choices = ['X','O']
    choice = None
    
    while choice not in valid_choices:
        os.system( 'cls' )
        choice = input('Player 1: Please enter your choice: ')
        
    print(choice)
    return choice

def redraw_board(my_board, value, position):
    my_board[position] = value
    draw_board(my_board)
    
    
    
p1_choice = get_user_choice()
redraw_board(my_board, 'X',2)

