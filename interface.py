import os
from env import DeliveryEnv
from agent import Agent
from grader import grade

# Required ENV variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

def run_task(level):
    print(f"[STEP] Running level: {level}")

    env = DeliveryEnv(level)
    state = env.reset()

    total_reward = 0

    while True:
        # simple logic (baseline)
        action = 0

        state, reward, done, _ = env.step(action)
        total_reward += reward

        if done:
            break

    score = grade(total_reward)

    print(f"[STEP] Score: {score}")
    return score


if __name__ == "__main__":
    print("[START] Inference started")

    levels = ["easy", "medium", "hard"]
    results = {}

    for lvl in levels:
        results[lvl] = run_task(lvl)

    print("[END] Inference completed")
    print("Results:", results)
