# 🚚 Delivery Route Optimization Environment

## 📌 Overview
This project implements an AI-compatible environment using the OpenEnv specification.  
The environment simulates a real-world delivery system where an agent selects optimal routes based on time and traffic conditions.

---

## 🎯 Objective
The goal is to minimize delivery time and traffic impact by choosing the best route, maximizing the reward.

---

## 🧠 Environment Design

### State
The state contains:
- `time`: Estimated delivery time
- `traffic`: Traffic level

Example:
```json
{"time": 5, "traffic": 3}
