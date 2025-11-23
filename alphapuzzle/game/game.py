class Game:
    def __init__(self, env, agent1, agent2):
        self.env = env
        self.agent1 = agent1
        self.agent2 = agent2

    def play(self):
        state = self.env.reset()
        done = False

        while not done:
            action1 = self.agent1.get_action(state)
            action2 = self.agent2.get_action(state)
            state, reward, done = self.env.step(action1, action2)

        return reward
