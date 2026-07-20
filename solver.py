# 1. Defined a working, valid sample grid
board = [
    [4, 6, 1, 7, 3, 9, 2, 5, 8],
    [2, 0, 0, 5, 8, 4, 1, 6, 9],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [1, 0, 2, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 1],
    [8, 4, 5, 2, 0, 0, 0, 0, 0],
    [6, 0, 0, 4, 9, 2, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 6, 0, 4],
    [7, 1, 4, 3, 5, 6, 8, 9, 2]
]

def print_board(bo):
    """Prints the board cleanly with grid separators."""
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    """Finds an empty cell (represented by 0) and returns its (row, col) coordinates."""
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(bo, num, pos):
    """Checks if a number placement is legal based on Sudoku rules."""
    # Check row constraint
    for j in range(len(bo[0])):
        if bo[pos[0]][j] == num and pos[1] != j:
            return False

    # Check column constraint
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 local box constraint
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(bo):
    """The recursive backtracking core engine that solves the puzzle."""
    find = find_empty(bo)
    if not find:
        return True  # No empty spaces left = Solved!
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0  # Crucial step: reset back to 0 on a dead end (Backtrack)

    return False

# 2. Execute and display results
print("🧩 ORIGINAL UNSOLVED BOARD:")
print_board(board)
print("\n" + "="*30 + "\n")

solve(board)

print("✅ SOLVED BOARD:")
print_board(board)