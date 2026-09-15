# Python3 program to solve N Queen
# Problem using backtracking

N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def isSafe(board, row, col):

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                     range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N),
                     range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col):

    # Base case: If all queens are placed
    if col >= N:
        return True

    # Try placing the queen in each row
    for i in range(N):

        if isSafe(board, i, col):

            # Place queen
            board[i][col] = 1

            # Recursively place remaining queens
            if solveNQUtil(board, col + 1):
                return True

            # Backtrack
            board[i][col] = 0

    return False


def solveNQ():

    board = [[0 for _ in range(N)] for _ in range(N)]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


# Driver Code
if __name__ == '__main__':
    solveNQ()
