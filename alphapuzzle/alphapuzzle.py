from env.environment import Environment
from agents.heuristic_agent import HeuristicAgent
from agents.value_network import ValueNetwork
from game.game import Game
from train.trainer import Trainer


def main():
    print("Starting AlphaPuzzle...")

    # 1. Create environment
    env = Environment()

    # 2. Create game
    game = Game(env)

    # 3. Create agents
    heuristic_agent = HeuristicAgent()
    value_network = ValueNetwork(input_size=9, hidden_size=128, output_size=1)

    # 4. Create trainer
    trainer = Trainer(agent=value_network, env=env)

    # 5. Run training
    print("Training Value Network...")
    trainer.train(episodes=1000)

    # 6. After training: Evaluate a puzzle
    print("Evaluating with trained Value Network...")
    sample_state = env.reset()
    value = value_network.evaluate(sample_state)
    print("Sample state value:", value)

    print("AlphaPuzzle completed.")


if __name__ == "__main__":
    main()
