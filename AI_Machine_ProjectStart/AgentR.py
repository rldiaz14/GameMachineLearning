import random

class RandomAgent:
    """
    This is Agent R (RandomAgent), the simplest agent. Its strategy is
    to pick an action completely at random from the available actions.

    It is mainly used as a baseline and for training other more complex
    agents such as Agent Q (Deep Q-learning agent). Even though it doesn't
    make use of any learned strategies or tactics, its randomness can sometimes
    lead to unexpected wins, making it a good starting point for training.
    """
    def __init__(self, action_size, name="AgentR"):
        """
        Constructor for the RandomAgent class.

        Args:
        action_size (int): The number of possible actions that the agent
        can take.

        name (str): Name of the agent. Default is "AgentR".
        """
        self.action_size = action_size
        self.name = name

    def get_action(self, state):
        """
        Method to determine the next action given the current state.
        For RandomAgent, it completely ignores the state and picks
        a random action.

        Args:
        state (array-like): Current state of the environment. Not used
        by this agent, but included for compatibility with other agents.

        Returns:
        action (int): A random valid action.
        """
        return random.randint(0, self.action_size - 1)