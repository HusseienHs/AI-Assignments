def base_heuristic(curr_state):
    def count_sequences(grid, player, seq_length, open_sides):
        rows, cols = grid.shape
        count = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for x in range(rows):
            for y in range(cols):
                if grid[x, y] == player:
                    for dx, dy in directions:
                        seq = []
                        left_open, right_open = False, False

                        for i in range(-1, seq_length + 1):
                            nx, ny = x + i * dx, y + i * dy
                            if 0 <= nx < rows and 0 <= ny < cols:
                                if 0 <= i < seq_length:
                                    seq.append(grid[nx, ny])
                                elif i == -1:
                                    left_open = grid[nx, ny] == 0
                                elif i == seq_length:
                                    right_open = grid[nx, ny] == 0
                            else:
                                if i == -1:
                                    left_open = False
                                elif i == seq_length:
                                    right_open = False

                        if seq.count(player) == seq_length and seq.count(0) == 0:
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

def advanced_heuristic(curr_state):
    return 0
