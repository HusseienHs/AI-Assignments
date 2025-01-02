import sys
from typing import Tuple

import numpy as np

if "../" not in sys.path:
    sys.path.append("../")


class ValueIteration:

    def __init__(self, prob_one: float, prob_three: float, prob_six: float, theta=0.0001, discount_factor=1.0):
        self.prob_one = prob_one
        self.prob_three = prob_three
        self.prob_six = prob_six
        self.theta = theta
        self.discount_factor = discount_factor


    def calculate_q_values(self, current_capital: int, value_function: np.ndarray, rewards: np.ndarray) -> np.ndarray:
        """
        Helper function to calculate the value for all action in a given state.

        Args:
            current_capital: The gambler’s capital. Integer. (state)
            value_function: The vector that contains values at each state. (the recursive value function)
            rewards: The reward vector. (the immediate reward according to the gambler's problem definition)

        Returns:
            A vector containing the expected value of each action in THIS state.
            Its length equals to the number of actions.
        """
        pass

        max_bet = min(current_capital, len(value_function) - 1 - current_capital)
        q_values = np.zeros(max_bet + 1)

        for bet in range(1, max_bet + 1):
            win_state = current_capital + bet
            lose_state = current_capital - bet

            q_values[bet] = (
                    self.prob_one * (rewards[win_state] + self.discount_factor * value_function[win_state]) +
                    self.prob_three * (rewards[lose_state] + self.discount_factor * value_function[lose_state]) +
                    self.prob_six * (rewards[current_capital] + self.discount_factor * value_function[current_capital])
            )

        return q_values

    def value_iteration_for_gamblers(self) -> Tuple[np.ndarray, np.ndarray]:
        """

        """
        max_capital = 100
        value_function = np.zeros(max_capital + 1)
        rewards = np.zeros(max_capital + 1)
        rewards[max_capital] = 1  # Reward for reaching the goal

        policy = np.zeros(max_capital + 1, dtype=int)

        while True:
            delta = 0

            for state in range(1, max_capital):
                q_values = self.calculate_q_values(state, value_function, rewards)
                best_action_value = np.max(q_values)

                delta = max(delta, abs(best_action_value - value_function[state]))
                value_function[state] = best_action_value

            if delta < self.theta:
                break

        for state in range(1, max_capital):
            q_values = self.calculate_q_values(state, value_function, rewards)
            policy[state] = np.argmax(q_values)

        return policy, value_function

