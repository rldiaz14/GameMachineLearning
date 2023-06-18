import numpy as np
from collections import defaultdict

class AgentM:
    def __init__(self, grid_size, epsilon=0.1, gamma=0.9):
        self.state_history = []
        self.V = defaultdict(float)  # State-value function
        self.returns = defaultdict(float) # Dictionary of returns
        self.returns_counts = defaultdict(int) # Dictionary of counts of return
        self.epsilon = epsilon # epsilon for exploration-exploitation trade-off
        self.gamma = gamma # Discount factor
        self.grid_size = grid_size

    def choose_action(self, state, available_actions):
        """
        This method chooses an action based on the epsilon-greedy policy
        """
        # Exploration-exploitation trade-off
        if np.random.uniform(0, 1) < self.epsilon:
            # Exploration: choose a random action from all available actions
            action = available_actions[np.random.choice(len(available_actions))]
        else:
            # Exploitation: choose the action with highest expected return
            q_values = [self.V[(state.tobytes(), a)] for a in available_actions]
            action = available_actions[np.argmax(q_values)]
        return action

    def update_return(self, reward):
        """
        This method updates the returns for the states in an episodes after it has ended
        """
        # Calculate return and update state values
        G = 0
        for t in range(len(self.state_history) - 1, -1, -1):
            state, action = self.state_history[t]
            G = self.gamma * G + reward
            self.returns[(state.tobytes(), action)] += G
            self.returns_counts[(state.tobytes(), action)] += 1
            self.V[(state.tobytes(), action)] = self.returns[(state.tobytes())]
        # Clear state history
        self.state_history = []

    def train(self, game, episodes, max_steps):
        """
        This method trains the agent for a given number of episodes and maximum steps per episode.
        """
        for episodes in range(episodes):
            state = game.reset()
            for step in range(max_steps):
                available_actions = available_actions(state)
                action = self.choose_action(state, available_actions)
                next_state, reward, done = game.step(action)
                # Add state and action to history
                self.state_history.append((state.tobytes(), action))
                if done:
                    self.update_return(reward)
                    break
                state = next_state  # Update state