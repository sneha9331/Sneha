N = int(input("Enter number of queens (N): "))

queen = "Q"
empty = "-"

# Initialize board
board = [[empty for _ in range(N)] for _ in range(N)]

# Check if position is safe
def is_safe(row, col):
    # Check column
    for i in range(row):
        if board[i][col] == queen:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == queen:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == queen:
            return False
    return True

# Solve using backtracking
def solve(row):
    if row == N:
        print("\nFinal Board:")
        print_board()
        return True
    
    for col in range(N):
        if is_safe(row, col):
            board[row][col] = queen
            print(f"\nPlacing queen at row {row}, column {col}")
            print_board()
            if solve(row + 1):
                return True
            board[row][col] = empty  # backtrack
            print(f"\nBacktracking from row {row}, column {col}")
            print_board()
    return False

# Print the board
def print_board():
    for i in board:
        print(" ".join(i))
    print()

# Main call
if not solve(0):
    print("No solution exists.")