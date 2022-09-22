"""
Assignment: Tic-Tac-Toe
Author: Evan Grizzle
"""

def main():
    again = ""
    taken_squares = []
    while again != "N":
        player = player_id()
        board = create_board()
        while not (game_won(board) or game_draw(board)):
            display_board(board)
            make_move(player, board, taken_squares)
            player = take_turn(player)

        display_board(board)
        again = input("Congrats on a Game well played. Would you Like to Play Again? (Y/N) ").upper()
    

def player_id():
    """ A Function that allows the player to choose
        to play as either X's or O's

        Parameters: None.
        Return: An ID string of the value "X" or a 
                value of "O".
    """
    id = ""
    while id != "X" or  id != "O":
        if id == "X":
            return id
        elif id == "O":
            return id
        else:
            id = input("Would you Like to Play as \"X\" or \"O\"? ").upper()

def create_board():
    """ A Function that creates and returns a varible
        that will be the playing field.

        Parameter: None.
        Return: An array.
    """
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def display_board(board):
    """ A Function that prints the current values on
        the game board.

        Parameter:
            board: The board array.
        Return: None.
    """
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("- + - + -")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("- + - + -")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def make_move(player, board, taken_squares):
    """ A function that asks the current player where
        they wish to make their move.

        Parameter:
            player: the current player. Should be a
                    value of either "x" or "o"
            board: the current board. Stored as an array.
            taken_squares: an array containing the squares 
                            that have already been taken by
                            a player.
        Return: None.
    """
    already_taken = True
    square = int(input(f"Player - {player}, choose a square (1-9) "))
    while already_taken:
        if square in taken_squares:
            print("Invalid Move. That Square has already been taken. Please select another Square")
            square = int(input(f"Player - {player}, choose a square (1-9) "))
            already_taken = True
        else: 
            taken_squares.append(square)
            board[square - 1] = player
            already_taken = False


def take_turn(current_player):
    """ A function that swaps from one player to the
        next.

        Parameter:
            current_player: The id of the current player.
                    Is either a value of "x" or "o"
        Return:
            next_player: The id of the player that 
                    is taking the next turn. Is 
                    either a value of "x" or "o".
    """
    next_player = ""
    if current_player == "X":
        next_player = "O"
        return next_player
    elif current_player == "O":
        next_player = "X"
        return next_player

def game_won(board):
    """ A Function that reviews the current state of
        the game board to check if one side has won.

        Parameter: 
            board: The game board stored as an array.
        Return: True if player has won.
    """
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


def game_draw(board):
    """ A Function that reviews the current state of
        the game board to check if a draw has occurred.

        Parameter: 
            board: The game board stored as an array.
        Return: True if the game has come to a draw.
                False if the game has not come to a draw.
    """
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True


if __name__ == "__main__":
    main()