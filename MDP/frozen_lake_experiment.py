from pathlib import Path

import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map

from full_solution.common import Params
from full_solution.plotting import plot_q_values_map
from full_solution.q_learning import Qlearning


params = Params(
    total_episodes=2000,
    learning_rate=0.5,
    gamma=0.95,
    epsilon=0.1,
    map_size=5,
    seed=42,
    is_slippery=False,
    n_runs=20,
    proba_frozen=0.9,
    savefig_folder=Path("../figures"),
)

if __name__ == '__main__':
    map_size = 3
    avg_rewards = []
    avg_steps = []
    # for _ in range(5):
    env = gym.make(
        "FrozenLake-v1",
        is_slippery=params.is_slippery,
        render_mode="rgb_array",
        desc=generate_random_map(
            size=map_size, p=params.proba_frozen, seed=params.seed
        ),
    )

    env.action_space.seed(params.seed)
    learner = Qlearning(
        learning_rate=params.learning_rate,
        gamma=params.gamma,
        state_size=env.observation_space.n,
        action_size=env.action_space.n,
        epsilon=params.epsilon,
    )
    total_rewards, total_steps = learner.run_environment(env=env, num_episodes=params.total_episodes)
    plot_q_values_map(learner.qtable, env, map_size)