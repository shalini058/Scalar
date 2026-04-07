import random

class DeliveryEnv:
    def __init__(self):
        self.routes = [
            {"time": 5, "traffic": 2},
            {"time": 8, "traffic": 1},
            {"time": 6, "traffic": 3}
        ]

        self.state_data = None
        self.steps = 0
        self.max_steps = 5

    def reset(self):
        self.steps = 0
        self.state_data = random.choice(self.routes)
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        """
        action = route index (0,1,2)
        """
        self.steps += 1
        chosen_route = self.routes[action]

        # reward logic
        reward = 1 / (chosen_route["time"] + chosen_route["traffic"])

        # next state
        self.state_data = random.choice(self.routes)

        done = self.steps >= self.max_steps
        return self.state(), reward, done, {}
