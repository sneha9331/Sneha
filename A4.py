from collections import deque

N = int(input("Enter number of queens (N): "))
method = input("Choose method - 'backtracking' or 'branch': ").strip().lower()

queen = "Q"
empty = "-"

# Initialize board
board = [[empty for _ in range(N)] for _ in range(N)]

# Print the board
def print_board(board_state):
    for row in board_state:
        print(" ".join(row))
    print()

# -----------------------------
# 1. Backtracking Method
# -----------------------------
def is_safe(row, col):
    for i in range(row):
        if board[i][col] == queen:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == queen:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == queen:
            return False
    return True

def backtracking_solve(row):
    if row == N:
        print("\nFinal Board (Backtracking):")
        print_board(board)
        return True
    
    for col in range(N):
        if is_safe(row, col):
            board[row][col] = queen
            print(f"\nPlacing queen at row {row}, column {col}")
            print_board(board)

            if backtracking_solve(row + 1):
                return True

            board[row][col] = empty
            print(f"\nBacktracking from row {row}, column {col}")
            print_board(board)
    return False

# -----------------------------
# 2. Branch and Bound (True BFS)
# -----------------------------
def is_promising(row, col, cols, diag1, diag2):
    return not cols[col] and not diag1[row + col] and not diag2[row - col + N - 1]

def branch_and_bound_bfs():
    queue = deque()
    init_board = [[empty for _ in range(N)] for _ in range(N)]
    queue.append((0, init_board, [False]*N, [False]*(2*N-1), [False]*(2*N-1)))

    while queue:
        row, b, cols, diag1, diag2 = queue.popleft()

        if row == N:
            print("\nFinal Board (Branch and Bound - BFS):")
            print_board(b)
            return True

        for col in range(N):
            d1 = row + col
            d2 = row - col + N - 1
            if is_promising(row, col, cols, diag1, diag2):
                new_board = [r[:] for r in b]
                new_board[row][col] = queen

                new_cols = cols[:]
                new_diag1 = diag1[:]
                new_diag2 = diag2[:]
                new_cols[col] = new_diag1[d1] = new_diag2[d2] = True

                print(f"\nPlacing queen at row {row}, column {col}")
                print_board(new_board)

                queue.append((row + 1, new_board, new_cols, new_diag1, new_diag2))

    print("No solution exists.")
    return False

# -----------------------------
# Main Method Call
# -----------------------------
if method == "backtracking":
    if not backtracking_solve(0):
        print("No solution exists.")
elif method == "branch":
    branch_and_bound_bfs()
else:
    print("Invalid method selected.")