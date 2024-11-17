# Autonomous Vehicle Traffic Flow Management using N-Queens Problem (Backtracking Solution)

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, N):
    # If all vehicles are placed
    if col >= N:
        return True

    # Try placing the vehicle in all rows one by one in this column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the vehicle
            board[i][col] = 1

            # Recur to place rest of the vehicles
            if solve_n_queens(board, col + 1, N):
                return True

            # Backtrack if placing the vehicle doesn't lead to a solution
            board[i][col] = 0

    # No safe placement was found for this column
    return False

def display_board(board, N):
    for row in range(N):
        print(" ".join("V" if board[row][col] == 1 else "." for col in range(N)))
    print("\n")

def autonomous_vehicle_traffic_flow(N):
    # Initialize board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Attempt to solve the problem
    if not solve_n_queens(board, 0, N):
        print("No solution exists")
        return

    # Display the board as a conflict-free traffic pattern
    print(f"Traffic Flow for {N} Autonomous Vehicles on a {N}x{N} Grid:")
    display_board(board, N)

# Driver code
N = 8  # For example, 8 vehicles on an 8x8 grid
autonomous_vehicle_traffic_flow(N)