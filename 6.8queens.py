""" Assignment 6 - 8 Queens using Backtracking """

# Place 8 queens so that none can attack another
N = 8
queen_rows = [-1] * N

def is_safe(row, col):
    for previous_col in range(col):
        previous_row = queen_rows[previous_col]

        # Same row or same diagonal means it is not safe
        if previous_row == row:
            return False
        if abs(previous_row - row) == abs(previous_col - col):
            return False

    return True

def place_queen(col):
    if col == N:
        return True

    for row in range(N):
        if is_safe(row, col):
            queen_rows[col] = row

            if place_queen(col + 1):
                return True

            queen_rows[col] = -1  # undo move and try another row

    return False

if place_queen(0):
    for row in range(N):
        line = ""
        for col in range(N):
            line += "Q " if queen_rows[col] == row else ". "
        print(line)
else:
    print("No solution found.")
