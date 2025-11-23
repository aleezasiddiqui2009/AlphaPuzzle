class Environment:
    """
    A simple placeholder environment.
    You can replace this later with your real puzzle logic.
    """

    def __init__(self):
        # Define the state space and action space size
        self.state = 0
        self.max_state = 10  # End after state reaches this value

    def reset(self):
        """
        Reset environment to the initial state.
        Returns the initial state.
        """
        self.state = 0
        return self.state

    def step(self, action):
        """
        Executes the action.
        Returns: next_state, reward, done
        """
        # Example: the action adds +1 or +2
        self.state += action

        # Reward logic (temporary)
        reward = 1 if self.state < self.max_state else 10

        # Check termination
        done = self.state >= self.max_state

        return self.state, reward, done

    def get_action_space(self):
        """
        Defines available actions.
        Example: action 1 = +1 step, action 2 = +2 steps.
        """
        return [1, 2]
