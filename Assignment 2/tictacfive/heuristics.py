def base_heuristic(curr_state):
    def count_sequences(grid, player, seq_length, open_sides):
        rows, cols = grid.shape
        count = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for x in range(rows):
            for y in range(cols):
                for dx, dy in directions:
                    sequence_count = 0
                    left_open, right_open = False, False

                    for i in range(-1, seq_length + 1):
                        nx, ny = x + i * dx, y + i * dy

                        if 0 <= nx < rows and 0 <= ny < cols:
                            if 0 <= i < seq_length:
                                if grid[nx, ny] == player:
                                    sequence_count += 1
                                else:
                                    break
                            elif i == -1:
                                left_open = grid[nx, ny] == 0
                            elif i == seq_length:
                                right_open = grid[nx, ny] == 0
                        else:
                            if i == -1:
                                left_open = False
                            elif i == seq_length:
                                right_open = False

                    # Ensure the sequence is exactly seq_length and not extendable
                    if sequence_count == seq_length:
                        # Check if the sequence is not part of a longer sequence
                        left_blocked = (0 <= x - dx < rows and 0 <= y - dy < cols and grid[x - dx, y - dy] == player)
                        right_blocked = (0 <= x + seq_length * dx < rows and 0 <= y + seq_length * dy < cols and grid[
                            x + seq_length * dx, y + seq_length * dy] == player)

                        if not (left_blocked or right_blocked):
                            if open_sides == 1 and (left_open or right_open):
                                count += 1
                            elif open_sides == 2 and left_open and right_open:
                                count += 1

        return count

    grid = curr_state.get_grid()
    player_1 = 1
    player_2 = 2

    # Compute heuristics for both players
    p1_score = (
        count_sequences(grid, player_1, 4, 1) +
        count_sequences(grid, player_1, 3, 2)
    )
    p2_score = (
        count_sequences(grid, player_2, 4, 1) +
        count_sequences(grid, player_2, 3, 2)
    )

    # Return the difference in heuristics
    return p1_score - p2_score

import numpy as np

def advanced_heuristic(curr_state):
    def count_sequences(grid, player, seq_length, open_sides):
        rows, cols = grid.shape
        count = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for dx, dy in directions:
            for x in range(rows):
                for y in range(cols):
                    if grid[x, y] == player:
                        left_open = False
                        right_open = False
                        sequence = []

                        # Check sequence along the direction
                        for i in range(-1, seq_length + 1):
                            nx, ny = x + i * dx, y + i * dy
                            if 0 <= nx < rows and 0 <= ny < cols:
                                if 0 <= i < seq_length:
                                    sequence.append(grid[nx, ny])
                                elif i == -1:
                                    left_open = grid[nx, ny] == 0
                                elif i == seq_length:
                                    right_open = grid[nx, ny] == 0
                            else:
                                if i == -1:
                                    left_open = False
                                elif i == seq_length:
                                    right_open = False

                        # Verify if sequence matches criteria
                        if sequence.count(player) == seq_length and sequence.count(0) == 0:
                            if open_sides == 1 and (left_open or right_open):
                                count += 1
                            elif open_sides == 2 and left_open and right_open:
                                count += 1

        return count

    # Grid and player information
    grid = curr_state.get_grid()
    player_1 = 1
    player_2 = 2

    # Precompute center bonus weights
    rows, cols = grid.shape
    center_weights = np.abs(
        np.indices((rows, cols)) - np.array([rows // 2, cols // 2])[:, None, None]
    ).sum(axis=0)

    def weighted_heuristic(player):
        # Calculate center bonus
        center_bonus = np.sum((grid == player) * center_weights)

        # Calculate threats and sequences
        threat_value = (
            count_sequences(grid, player, 4, 1) * 10 +
            count_sequences(grid, player, 4, 2) * 5 +
            count_sequences(grid, player, 3, 2) * 2
        )

        return center_bonus + threat_value

    # Compute heuristic scores for both players
    p1_score = weighted_heuristic(player_1)
    p2_score = weighted_heuristic(player_2)

    return p1_score - p2_score
