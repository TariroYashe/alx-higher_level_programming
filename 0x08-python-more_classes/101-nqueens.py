#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def format_solution(board):
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        return solution

    def print_solutions(solutions):
        for solution in solutions:
            print(solution)
        print()

    def solve(board, col, solutions):
        if col == N:
            solutions.append(format_solution(board))
            return
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve(board, col + 1, solutions)
                board[i][col] = 0

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0, solutions)
    print_solutions(solutions)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    solve_nqueens(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)