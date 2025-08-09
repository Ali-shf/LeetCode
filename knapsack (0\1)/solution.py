def knapsack(weights, values, capacity):
    n = len(weights)
    grid = [[0] * (capacity + 1) for _ in range(n + 1)]
    for row in range(1, n + 1):
        for col in range(1, capacity + 1):
            if weights[row - 1] <= col:
                grid[row][col] = max(grid[row - 1][col], grid[row - 1][col - weights[row - 1]] + values[row - 1])
            else:
                grid[row][col] = grid[row - 1][col]
    return grid[n][capacity]




