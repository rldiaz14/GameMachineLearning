from Game import Game
from AgentQ import AgentQ
from AgentR import RandomAgent


def main():
    # Parameters
    episodes = 1000 # Number of games to train on
    max_steps = 9

    # Create objects
    game = Game()
    agent = AgentQ(grid_size=3, epsilon=0.2, alpha=0.5, gamma=0.9)

    # Train the agent
    agent.train(game, episodes, max_steps)

    # Evaluate the agent
    agent.epsilon = 0 # Turn off exploration
    state = game.reset()
    done = False
    while not done:
        available_actions = game.available_actions()
        action = agent.choose_action(state, available_actions)
        next_state, reward, done = game.step(action)
        state = next_state

    # Print the result
    game.render()
    print(f'Reward: {reward}')
    
if __name__ == "__main__":
    main()