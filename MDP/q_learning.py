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
        """Update the Q-table."""
        max_future_q = np.max(self.qtable[new_state])
        self.qtable[state, action] += self.learning_rate * (
                    reward + self.gamma * max_future_q - self.qtable[state, action])

    def reset_qtable(self):
        """Reset the Q-table."""
        self.qtable = np.zeros((self.state_size, self.action_space_size))

    def select_epsilon_greedy_action(self, state: int) -> int:
        """Select an action using epsilon-greedy policy."""
        if rng.random() < self.epsilon:
            return rng.integers(self.action_space_size)
        else:
            max_qvalue = np.max(self.qtable[state])
            optimal_actions = np.where(self.qtable[state] == max_qvalue)[0]
            return rng.choice(optimal_actions)  # Corrected to use rng.choice

    def train_episode(self, env: gym.Env) -> Tuple[float, int]:
        """Train the agent for a single episode."""
        state, _ = env.reset(seed=SEED)
        cumulative_reward = 0.0
        steps = 0
        done = False

        while not done:
            action = self.select_epsilon_greedy_action(state)
            new_state, reward, done, truncated, info = env.step(action)
            self.update(state, action, reward, new_state)
            cumulative_reward += reward
            steps += 1
            state = new_state

        return cumulative_reward, steps

    def run_environment(self, env: gym.Env, num_episodes: int) -> Tuple[List[float], List[int]]:
        """Run the environment with the given policy."""
        total_rewards = []
        total_steps = []

        for ep in range(num_episodes):
            total_reward, steps = self.train_episode(env)
            total_rewards.append(total_reward)
            total_steps.append(steps)

        return total_rewards, total_steps
