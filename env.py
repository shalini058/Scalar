import random

class DeliveryEnv:

    def __init__(self, level="easy"):
        # Different difficulty levels
        if level == "easy":
            self.routes = [
                {"time": 5, "traffic": 1},
                {"time": 6, "traffic": 2}
            ]
        elif level == "medium":
            self.routes = [
                {"time": 5, "traffic": 3},
                {"time": 8, "traffic": 2},
                {"time": 6, "traffic": 4}
            ]
        else:  # hard
            self.routes = [
                {"time": 10, "traffic": 5},
                {"time": 7, "traffic": 6},
                {"time": 12, "traffic": 4},
                {"time": 9, "traffic": 7}
            ]

        self.state_data = None
        self.steps = 0
        self.max_steps = 5

    # Reset environment
    def reset(self):
        self.steps = 0
        self.state_data = random.choice(self.routes)
        return self.state()

    # Return current state
    def state(self):
        return self.state_data

    # Take action
    def step(self, action):
        """
        action = route index (0,1,2,...)
        """

        self.steps += 1

        # Safety check (important)
        if action < 0 or action >= len(self.routes):
            reward = 0
            done = True
            return self.state(), reward, done, {"error": "Invalid action"}

        chosen_route = self.routes[action]

        # Reward function (normalized)
        reward = 1 / (chosen_route["time"] + chosen_route["traffic"])

        # Move to next state
        self.state_data = random.choice(self.routes)

        # Episode end
        done = self.steps >= self.max_steps

        return self.state(), reward, done, {}
