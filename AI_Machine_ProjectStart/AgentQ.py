from collections import defaultdict
import numpy as np
import pickle



class AgentQ:
    def __init__(self, grid_size, epsilon=0.2, alpha=0.5, gamma=0.9):
        """"
        This method initializes the agent. It's the constructor for the agent class.
        """
        self.state_history = []
        self.Q = defaultdict(float)
        self.epsilon = epsilon # epsilon for exploration-exploitation trade-off
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor
        self.grid_size = grid_size

    def get_max_q_value_action(self, state, available_actions):
        """
        This method returns the action (from all possible actions) that has the maximum Q value for a given state.
        """
        max_q_val = -np.inf
        best_action = None
        for action in available_actions:
            q_val = self.Q[(state.tobytes(), action)]
            if q_val > max_q_val:
                max_q_val = q_val
                best_action = action
        return max_q_val, best_action


    def choose_action(self, state, available_actions):
        """
        This method chooses an action based on the epsilon-greedy policy (a mix of taking the best action
        and exploring new actions).
        """
        # Exploration-exploitation trade-off
        if np.random.uniform(0, 1) < self.epsilon:
            # Exploration: choose a random action from all available actions
            action = available_actions[np.random.choice(len(available_actions))]
        else:
            # Exploitation : choose the action from all available actions
            _, action = self.get_max_q_value_action(state, available_actions)
            if action not in available_actions:
                action = available_actions[np.random.choice(len(available_actions))]
        return action


    def available_actions(self):
        """
        This method returns available actions for a given state.
        """
        return [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.state[i][j] == 0]

    def update_q_value(self, state, action, reward, next_state, done, available_actions):
        """
        This method updates the Q value of a (state, action) pair based on the reward received
        and the maximum Q value of the next state.
        """

        if done:
            max_q_next = 0
        else:
            max_q_next, _ = self.get_max_q_value_action(next_state, available_actions)
        self.Q[(state.tobytes(), action)] = self.Q[(state.tobytes(), action)] + \
                                            self.alpha * (reward + self.gamma * max_q_next - \
                                            self.Q[(state.tobytes(), action)])

    def train(self, game, episodes, max_steps):
        """
        This method trains the agent for a given number of episodes and maximum steps per episode.
        """
        for episodes in range(episodes):
            state = game.reset()
            for step in range(max_steps):
                available_actions = game.available_actions()
                action = self.choose_action(state, available_actions)
                next_state, reward, done = game.step(action)
                self.update_q_value(state, action, reward, next_state, done, available_actions)
                if done:
                    break
                state = next_state # update state with next_state
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