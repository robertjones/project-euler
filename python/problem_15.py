def sum_routes(node_width):
    grid = [[None]*node_width]*node_width
    for r in range(node_width):
        for c in range(node_width):
            grid[r][c] = 1 if (c == 0 or r == 0) else grid[r-1][c] + grid[r][c-1]
    return grid[-1][-1]

print(sum_routes(21)) # 21 nodes across for 20x20 squares