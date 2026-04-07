def __init__(self, level="easy"):
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

    self.steps = 0
    self.max_steps = 5
