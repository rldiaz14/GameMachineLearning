"""
This was second step of phase 1 for making the game of tic-tac-toc.
1. Making the code was fun because is working well creating board.
2. The board is 3 x 3
3. Using row, column and  number for to make the marked on the board.
4. The logic of this code is use X and O simple game of tic-tac-toe.
5. The implementation of the  minimax algorithm show the AI agent how to look for the best strategy of move to win.
6. After few hours of research, I decided to take this to Unity.
"""




""""
# Initialize an empty board
from AI_Machine_ProjectStart.GameSave import save_gameplay_to_file

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print('\n'.join([' | '.join(row) for row in board]))

def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def check_win(board):
    # Horizontal checks
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
    # Vertical check
    for col in range(3):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True
    # Diagonal check. Note that it's NOT inside the vertical checking loop
    if (board[0][0] == board[1][1] == board[2][2] != ' ' or
        board[0][2] == board[1][1] == board[2][0] != ' '):
        return True
    return False



def game():
    player = 'X'
    player_moves = { 'X': [], 'O': [] } # To record each player's moves
    for _ in range(9):
        while True:
            print_board(board)
            row = get_valid_input("Enter the row for player " + player + ": ")
            col = get_valid_input("Enter the column for player " + player + ": ")
            if make_move(board, row, col, player):
                player_moves[player].append((row, col)) # Record the move
                break
        if check_win(board):
            print("Player " + player + " wins!")
            save_gameplay_to_file(player, "Win", board, player_moves[player]) # Save winner's gameplay
            break
        player = 'O' if player == 'X' else 'X'
    else:
        print_board(board)
        print("It's a draw")
        save_gameplay_to_file('X', "Draw", board, player_moves['X']) # Save both players' gameplay
        save_gameplay_to_file('O', "Draw", board, player_moves['O'])


def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 2:
                return value
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the game
game()"""