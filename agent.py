import random

class Agent:
    def choose_action(self, routes):
        best_action = 0
        best_score = float('inf')

        for i, r in enumerate(routes):
            score = r["time"] + r["traffic"]
            if score < best_score:
                best_score = score
                best_action = i

        return best_action
