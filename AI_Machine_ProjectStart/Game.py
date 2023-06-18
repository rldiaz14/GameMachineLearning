import random
import numpy as np


class Game:
    def __init__(self):
        """
        This method initializes the game/board. It's the constructor for the Game class.
        """
        self.board = np.zeros((3, 3))
        self.current_winner = None

    def reset(self):
        """
        This method resets the game/board to the initial state.
        """
        self.board = np.zeros((3, 3))
        self.current_winner = None
        return self.board.copy()

    def available_actions(self):
        """
        Return a list of available actions.
        """
        return [(i, j) for i in range(self.board.shape[0]) for j in range(self.board.shape[1]) if self.board[i, j] == 0]

    def step(self, action1, action2):
        """
        This method applies an action (placing 'X' or 'O' on the board). It returns the next state, reward and whether
        the game has ended.
        """
        # Agent Q's move
        self.board[action1] = 1 # Agent's move
        reward1 = self.get_reward()
        done = self.check_game_over()

        # Environment's move
        if done:
            return self.board.copy(), reward1, -reward1, done

        # Agent M's move
        self.board[action2] = -1 # AgentM's move
        reward2 = self.get_reward()
        done = self.check_game_over()

        return self.board.copy(), -reward2, reward2, done
    def get_reward(self):
        """
        Checks if the game has a winner and returns appropriate reward.
        """
        if self.check_winner():
            return 1
        elif self.is_board_full():
            return 0.5 # draw
        else:
            return 0 # No result yet

    def check_winner(self):
        """
        This method checks if there's a winner (three 'X's or 'O's in a row in any direction)
        """
        # Check horizontal lines
        for row in self.board:
            if np.all(row == 1):
                self.current_winner = 1
                return True
            if np.all(row == -1):
                self.current_winner = -1
                return True

        # Check vertical lines
        for col in self.board.T:
            if np.all(col == 1):
                self.current_winner = 1
                return True
            if np.all(col == -1):
                self.current_winner = -1
                return True

        # Check main diagonal
        if np.all(np.diag(self.board) == 1) or np.all(np.diag(np.flipud(self.board)) == 1):
            self.current_winner = 1
            return True

        if np.all(np.diag(self.board) == -1) or np.all(np.diag(np.flipud(self.board)) == -1):
            self.current_winner = -1
            return True

        return False


    def check_game_over(self):
        """
        This method check if the game is over, which can be when there is a winner or the board is full.
        """
        if self.check_winner() or self.is_board_full():
            return True
        return False

    def is_board_full(self):
        """
        This method checks if the board is full (i.e., there are no more moves left).
        """
        return not (0 in self.board)

    def render(self):
        """
        This method prints the current board state in a way that's easy for humans to understand.
        """
        symbol = {1: 'X', -1: 'O', 0: ' '}
        board_visual = np.vectorize(symbol.get)(self.board)
        print(board_visual)



