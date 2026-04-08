import gradio as gr
from env import DeliveryEnv
from agent import Agent
from grader import grade

def run_simulation(level):
    if not level:
        return "Please select a level"

    env = DeliveryEnv(level)
    agent = Agent()

    state = env.reset()
    total_reward = 0
    output = ""
    step_count = 1

    while True:
        action = agent.choose_action(env.routes)

        state, reward, done, _ = env.step(action)

        output += f"Step {step_count}: Action {action}, Reward {round(reward,3)}\n"
        total_reward += reward
        step_count += 1

        if done:
            break

    score = grade(total_reward)

    output += f"\nTotal Reward: {round(total_reward,3)}\n"
    output += f"Final Score: {score}"

    return output


demo = gr.Interface(
    fn=run_simulation,
    inputs=gr.Dropdown(["easy", "medium", "hard"], label="Select Level", value="easy"),
    outputs="text",
    title=" Delivery Route Optimization AI",
    description="Choose difficulty and run AI simulation"
)

if __name__ == "__main__":
    demo.launch()
