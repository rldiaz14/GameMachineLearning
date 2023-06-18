from Game import Game
from AgentQ import AgentQ
from AgentM import AgentM

def main_agent_battle():
    # Parameters
    episodes = 1000 # Number of games to play
    max_steps = 9

    game = Game()
    agent_q = AgentQ(grid_size=3, epsilon=0.2, alpha=0.5, gamma=0.9)
    agent_m = AgentM(grid_size=3)

    # Train the agent
    agent_q.train(game, episodes, max_steps)

    # Evaluate the agents
    agent_q.epsilon = 0 # Turn of exploration
    state = game.reset()
    done = False
    while not done:
        available_actions = game.available_actions()

        # Agent Q's turn
        action_q = agent_q.choose_action(state, available_actions)
        state, reward, done = game.step(action_q, player='Q')
        if done:
            break

        available_actions = game.available_actions()

        # Agent M's turn
        action_m = agent_m.choose_action(state, available_actions)
        state, reward, done = game.step(action_m, player='M')

    # Print the result
    game.render()
    print(f'Reward: {reward}')

    if __name__ == "__main__":
        main_agent_battle()