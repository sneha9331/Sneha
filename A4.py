N = int(input("Enter number of queens (N): "))
method = input("Choose method - 'backtracking' or 'branch': ").strip().lower()

queen = "Q"
empty = "-"

# Initialize board
board = [[empty for _ in range(N)] for _ in range(N)]

# Print the board
def print_board():
    for i in board:
        print(" ".join(i))
    print()

# 1. Backtracking method
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

def backtracking_solve(row):
    if row == N:
        print("\nFinal Board (Backtracking):")
        print_board()
        return True
    
    for col in range(N):
        if is_safe(row, col):
            board[row][col] = queen
            print(f"\nPlacing queen at row {row}, column {col}")
            print_board()
            if backtracking_solve(row + 1):
                return True
            board[row][col] = empty  # backtrack
            print(f"\nBacktracking from row {row}, column {col}")
            print_board()
    return False

# 2. Branch and Bound method
cols = [False] * N
diag1 = [False] * (2 * N - 1)  # row + col
diag2 = [False] * (2 * N - 1)  # row - col + N - 1

def branch_and_bound_solve(row):
    if row == N:
        print("\nFinal Board (Branch and Bound):")
        print_board()
        return True

    for col in range(N):
        d1 = row + col
        d2 = row - col + N - 1
        if not cols[col] and not diag1[d1] and not diag2[d2]:
            board[row][col] = queen
            cols[col] = diag1[d1] = diag2[d2] = True

            print(f"\nPlacing queen at row {row}, column {col}")
            print_board()

            if branch_and_bound_solve(row + 1):
                return True

            board[row][col] = empty
            cols[col] = diag1[d1] = diag2[d2] = False

            print(f"\nBacktracking from row {row}, column {col}")
            print_board()
    return False

# Main call
if method == "backtracking":
    if not backtracking_solve(0):
        print("No solution exists.")
elif method == "branch":
    if not branch_and_bound_solve(0):
        print("No solution exists.")
else:
    print("Invalid method selected.")
