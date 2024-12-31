from typing import List, Tuple

import gymnasium as gym
import numpy as np

SEED = 42

# Set the seed
rng = np.random.default_rng(SEED)


class Qlearning:
    def __init__(self, learning_rate: float, gamma: float, state_size: int, action_size: int, epsilon: float):
        self.state_size = state_size
        self.action_space_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.qtable = np.zeros((state_size, action_size))

    def update(self, state: int, action: int, reward: float, new_state: int):
        """In this function you need to implement the update of the Q-table.

        Args:
            state (int): Current state
            action (int): Action taken in the current state
            reward (float): Reward received after taking the action
            new_state (int): New state reached after taking the action.
        """
        max_future_q = np.max(self.qtable[new_state])
        self.qtable[state, action] += self.learning_rate * (reward + self.gamma * max_future_q - self.qtable[state, action])

    def reset_qtable(self):
        """Reset the Q-table."""
        self.qtable = np.zeros((self.state_size, self.action_space_size))

    def select_epsilon_greedy_action(self, state: int) -> int:
        """Select an action from the Q-table."""
        if rng.random() < self.epsilon:
            return rng.integers(self.action_space_size)
        else:
            max_qvalue = np.max(self.qtable[state])
            optimal = np.where(self.qtable[state] == max_qvalue)[0]
            return np.choice(optimal)


    def train_episode(self, env: gym.Env) -> Tuple[float, int]:
        """Train the agent for a single episode.

        Notice an episode is a single run of the environment until the agent reaches a terminal state
        (the return value of env.step() is True for the third and fourth elements)


        :param env: The environment to train the agent on.
        :return: the cumulative reward obtained during the episode and the number of steps executed in the episode.
        """
        state, _ = env.reset(seed=SEED)  # Reset the environment and get the initial state
        cumulative_reward = 0.0
        steps = 0
        done = False

        while not done:
            # Select an action using the epsilon-greedy policy
            action = self.select_epsilon_greedy_action(state)

            # Take the action in the environment
            new_state, reward, done, truncated, info = env.step(action)

            # Update the Q-table using the observed transition
            self.update(state, action, reward, new_state)

            # Update cumulative reward and step count
            cumulative_reward += reward
            steps += 1

            # Move to the next state
            state = new_state

        return cumulative_reward, steps


    def run_environment(self, env: gym.Env, num_episodes: int) -> Tuple[List[float], List[int]]:
        """
        Run the environment with the given policy.

        Args:
            env (gym.Env): The environment to train the agent on.
            num_episodes (int): The number of episodes to run the environment.

        Returns:
            A tuple (total_rewards, total_steps).
        """ 
        total_rewards = []
        total_steps = []
        
        for ep in range(num_episodes):
            total_reward, steps = self.train_episode(env)
            total_rewards.append(total_reward)
            total_steps.append(steps)
        return total_rewards, total_steps