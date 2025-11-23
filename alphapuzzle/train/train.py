class Trainer:
    def __init__(self, agent, env, episodes=1000):
        self.agent = agent
        self.env = env
        self.episodes = episodes

    def train(self):
        for episode in range(self.episodes):
            state = self.env.reset()
            done = False

            while not done:
                action = self.agent.get_action(state)
                next_state, reward, done = self.env.step(action)
                self.agent.learn(state, action, reward, next_state)
                state = next_state

        print("Training completed.")
