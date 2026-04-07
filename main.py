from env import DeliveryEnv
from agent import Agent

env = DeliveryEnv("easy")
agent = Agent()

state = env.reset()
total_reward = 0

while True:
    action = agent.choose_action(env.routes)
    
    state, reward, done, _ = env.step(action)

    total_reward += reward
    print(f"Action: {action}, Reward: {reward:.3f}")

    if done:
        break

print("Total Reward:", total_reward)
