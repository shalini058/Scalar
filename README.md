# Delivery Route Optimization Environment

## Description
This environment simulates delivery route decisions where an agent selects the best route based on time and traffic.

## Actions
- 0: Route A
- 1: Route B
- 2: Route C

## Observations
- time: delivery time
- traffic: traffic level

## Reward
Reward = 1 / (time + traffic)

## Run
python main.py
