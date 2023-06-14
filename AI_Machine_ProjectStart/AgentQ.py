import random
from collections import defaultdict
import numpy as np
import pickle



class AgentQ:
    def __init__(self, epsilon=0.2, alpha=0.5, gamma=0.9):
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
        max_q_val = -np.inf
        best_action = None
        for action in self.available_actions(state):
            q_val = self.Q[(state, action)]
            if q_val > max_q_val:
                max_q_val = q_val
                best_action = action
        return max_q_val, best_action
    def choose_action(self, state_tuple, available_actions):
        """
        This method chooses an action based on the epsilon-greedy policy (a mix of taking the best action
        and exploring new actions).
        """
        # Exploration-exploitation trade-off
        if np.random.uniform(0, 1) < self.epsilon:
            # Exploration: choose a random action from all available actions
            action = np.random.choice(available_actions)
        else:
            # Exploitation: choose the action with max Q-value for the current state
            _, best_action = self.get_max_q_value_action(state_tuple)
            if best_action in available_actions:
                action = best_action
            else:
                action = np.random.choice(available_actions)
        return action



    def available_actions(self, state_tuple):
        """
        This method returns available actions for a given state.
        """
        return np.where(np.array(state_tuple) == 0)[0]


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

    def train(self, game, episodes, max_steps):
        """
        This method trains the agent for a given number of episodes and maximum steps per episode.
        """
        for episode in range(episodes):
            state = game.reset()
            state_tuple = tuple(state.flatten())  # converting state to a tuple

            for step in range(max_steps):
                available_actions = self.available_actions(state)
                action = self.choose_action(state_tuple, available_actions)

                next_state, reward, done = game.step(action)
                next_state_tuple = tuple(next_state.flatten())  # converting next_state to a tuple

                # Q-learning formula
                best_q_value_next, _ = self.get_max_q_value_action(next_state_tuple)
                self.Q[(state_tuple, action)] = self.Q.get((state_tuple, action), 0) + \
                                                self.alpha * (reward + self.gamma * best_q_value_next -
                                                              self.Q.get((state_tuple, action), 0))

                if done:
                    break

                state_tuple = next_state_tuple  # update state_tuple with next_state_tuple

    def save_model(self, filepath):
        """
        This method saves the current state-action value (Q value) estimates to a file.
        """
        with open(filepath, 'wb') as f:
            pickle.dump(self.Q, f)

    def load_model(self, filepath):
        """
        This method loads state-action value (Q value) estimates from a file.
        """
        with open(filepath, 'rb') as f:
            self.Q = pickle.load(f)