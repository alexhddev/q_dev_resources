# Tic-Tac-Toe Game

class TicTacToe:
    """
    A class representing a Tic-Tac-Toe game.

    This class implements the game logic for a standard 3x3 Tic-Tac-Toe board.
    Players take turns placing 'X' and 'O' markers on the board until one player
    wins or the game ends in a tie.

    Attributes:
        board (list): A list of 9 elements representing the 3x3 game board.
                     Empty spaces are represented by ' '.
        current_player (str): Keeps track of whose turn it is ('X' or 'O').
    """    
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        # Check rows, columns and diagonals
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None

    def print_board(self):
        for i in range(0, 9, 3):
            print(' | '.join(self.board[i:i+3]))
            if i < 6:
                print('---------')

def play_game():
    """
    Main game loop function that handles the gameplay of Tic-Tac-Toe.

    This function creates a new TicTacToe game instance and manages the game flow by:
    - Displaying the current board state
    - Getting player moves via input
    - Validating moves
    - Making moves and checking for a winner
    - Handling invalid inputs
    - Announcing the game result

    The game continues until there is either a winner or a tie.

    Returns:
        None
    """    
    game = TicTacToe()
    winner = None

    while not winner:
        game.print_board()
        try:
            move = int(input(f"Player {game.current_player}, enter your move (0-8): "))
            if 0 <= move <= 8:
                if game.make_move(move):
                    winner = game.check_winner()
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Invalid move. Please enter a number between 0 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    game.print_board()
    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

if __name__ == "__main__":
    play_game()