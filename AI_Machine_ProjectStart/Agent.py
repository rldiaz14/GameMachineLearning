import random
from collections import defaultdict

import numpy as np


class Agent:
    def __int__(self, epsilon=0.2, alpha=0.5, gamma=0.9):
        """"
        This method initializes the agent. It's the constructor for the agent class.
        """
        self.state_history = []
        self.Q = defaultdict(float)
        self.epsilon = epsilon # epsilon for exploration-exploitation trade-off
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor
    def get_max_q_value_action(self, state):
        """
        This method returns the action (from all possible actions) that has the maximum Q value for a given state.
        """
        max_q_val = np.inf
        best_action = None
        for action in self.available_action(state):
            q_val = self.Q[(state, action)]
            if q_val > max_q_val:
                max_q_val = q_val
                best_action = action
        return max_q_val, best_action
    def choose_action(self, state, available_actions):
        """
        This method chooses an action based on the epsilon-greedy policy (a mix of taking the best action
        and exploring new actions).
        """
        if random.random() < self.epsilon:
            return random.choice(available_actions)
        else:
            _, best_action = self.get_max_q_value_action(state)
            return best_action

    def available_actions(self, state):
        """
        This method returns available actions for a given state.
        """
        # To do
        pass

    def update_q_value(self, state, action, reward, next_state, done):
        """
        This method updates the Q value of a (state, action) pair based on the reward received
        and the maximum Q value of the next state.
        """

        if done:
            max_q_next = 0
        else:
            max_q_next, _ = self.get_max_q_value_action(next_state)
        self.Q[(state, action)] = self.Q[(state, action)] + self.alpha * (reward + self.gamma * max_q_next - self.Q[(state, action)])

    def train(self, episodes, max_steps):
        """
        This method trains the agent for a given number of episodes and maximum steps per episode.
        """
        # to do
        pass

    def save_model(self, filepath):
        """
        This method saves the current state-action value (Q value) estimates to a file.
        """
        # To do
        pass

    def load_model(self, filepath):
        """
        This method loads state-action value (Q value) estimates from a file.
        """
        # To do
        pass