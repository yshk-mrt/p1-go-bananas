# Project 1: Navigation - Go Bananas!

### Introduction

This project aimed at solving [Navigation project at Udacity/Deep-Reinforcement-Learning](https://github.com/udacity/deep-reinforcement-learning/tree/master/p1_navigation).

An agent is trained to collect as many bananas as possible in a large, square world.

![Trained Agent](./results/05_screenShots/score16/banana_16.gif?raw=true "Trained Agent")

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and one episode consists of 300 steps. In order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

### Getting Started

1. To setup the basic environment, please follow the instruction below.
 - https://github.com/udacity/deep-reinforcement-learning/blob/master/README.md
 - https://github.com/udacity/deep-reinforcement-learning/blob/master/p1_navigation/README.md
2. After you can successfully run [Navigation.ipynb](https://github.com/udacity/deep-reinforcement-learning/blob/master/p1_navigation/Navigation.ipynb) on your environment, clone the repository.

3. Copy the Banana.app file at `p1_navigation/` into the `p1_go_bananas/` folder. 

### Instructions

- `TrainAgent.ipynb`trains agent and see the behavior of the trained agent.
- `Report.ipynb` describes detailes of trained models, results and future ideas.
