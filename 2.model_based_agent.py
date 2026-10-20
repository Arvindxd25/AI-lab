""" Assignment 2 - Model-Based Agent (Grid Navigation) """

# Model-based agent: remembers visited cells and avoids obstacles
from collections import deque

grid = [
    ["S", ".", "X", "."],
    ["X", ".", "X", "."],
    [".", ".", ".", "."],
    ["X", "X", ".", "G"]
]

rows, cols = len(grid), len(grid[0])
start = (0, 0)
goal = (3, 3)

queue = deque([(start, [start])])
visited = {start}
path = None

while queue:
    (row, col), current_path = queue.popleft()

    if (row, col) == goal:
        path = current_path
        break

    # Check nearby cells: right, down, left, up
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = row + dr, col + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] != "X" and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), current_path + [(nr, nc)]))

if path:
    print("Path to goal:", path)
    print("Cells remembered by the agent:", len(visited))
else:
    print("No path found.")
