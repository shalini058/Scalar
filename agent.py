import random

class Agent:
    def choose_action(self, state):
        best_action = 0
        best_score = float('inf')

        routes = [
            {"time": 5, "traffic": 2},
            {"time": 8, "traffic": 1},
            {"time": 6, "traffic": 3}
        ]

        for i, r in enumerate(routes):
            score = r["time"] + r["traffic"]
            if score < best_score:
                best_score = score
                best_action = i

        return best_action
