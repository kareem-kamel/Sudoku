import tkinter as tk
from queue import PriorityQueue

GRID_SIZE = 9

# Print the Sudoku grid in a readable format
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Check if placing num in (row, col) is safe
def is_safe(grid, row, col, num):
    # Check row and column
    if num in grid[row] or num in [grid[i][col] for i in range(GRID_SIZE)]:
        return False
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

# Find the next empty cell (marked by 0)
def find_empty(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:
                return row, col
    return None

# Solve the Sudoku puzzle with a UCS-based approach
def solve_sudoku(grid):
    queue = PriorityQueue()
    queue.put((0, grid))  # Initial grid with cost 0

    while not queue.empty():
        cost, current_grid = queue.get()
        
        # Locate an empty cell
        empty = find_empty(current_grid)
        if not empty:
            return current_grid  # Puzzle solved
        
        row, col = empty

        # Attempt numbers 1-9 in the empty cell
        for num in range(1, GRID_SIZE + 1):
            if is_safe(current_grid, row, col, num):
                # Create a new grid with the updated number
                new_grid = [r[:] for r in current_grid]
                new_grid[row][col] = num
                queue.put((cost + 1, new_grid))  # Place in queue with cost incremented

    return None  # Return None if no solution exists

# Define the initial puzzle state
initial_grid = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
]

# Solve and display the solution
solution = solve_sudoku(initial_grid)
if solution:
    print("Solved Sudoku:")
    print_grid(solution)
else:
    print("No solution exists :(")