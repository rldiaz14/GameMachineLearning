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

    def step(self, action):
        """
        This method applies an action (placing 'X' or 'O' on the board). It returns the next state, reward and whether the game has ended.
        """
        # Action will be a tuple (i, j), i.e, where to place 'X' or 'O'
        self.board[action] = 1 # Assuming '1' for the agent and ' -1' for the opponent
        reward = self.get_reward()
        done = self.check_game_over()
        return self.board.copy(), reward, done

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

        #  To do
        pass

    def is_board_full(self):
        """
        This method checks if the board is full (i.e., there are no more moves left).
        """
        return not (0 in self.board)

    def render(self):
        """
        This method prints the current board state in a way that's easy for humans to understand.
        """
        print(self.board)



