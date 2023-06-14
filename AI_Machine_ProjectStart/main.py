from Game import Game
from AgentQ import AgentQ
from AgentR import RandomAgent


def main():
    # Create a game instance
    game = Game()

    # Create an agent instance
    agent = AgentQ(epsilon=0.2, alpha=0.5, gamma=0.9)

    # Create an agent instance
    opponent = RandomAgent(action_size=9)

    # Number of episodes for training
    episode = 1000

    # Max steps per episode
    max_steps = 10

    # Train the agent
    agent.train(game, episode, max_steps)

    # Save the Learned Q-Values
    agent.save_model("model.json")

    # Test the agent
    # Load the Learned Q-Values
    agent.load_model("model.json")

    # Play a game and render the states
    done = False
    state = game.reset()
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = game.step(action)
        state = next_state
        game.render()

if __name__ == "__main__":
    main()