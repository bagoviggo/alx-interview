#!/usr/bin/python3
import sys
"""
N-Queens Solver


This program solves the N-Queens problem,
which is the challenge of placing N non-attacking queens
on an N×N chessboard.
"""


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a given position.

    Args:
        board (list of lists): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Find all solutions to the N-queens problem for a given board size.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list of lists: A list of solutions, each represented as a list of queen positions.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve(board, col):
        if col == n:
            solutions.append([row[:] for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    solutions = []
    solve(board, 0)
    return solutions


def print_solutions(solutions):
    """
    Print all the solutions found for the N-queens problem.

    Args:
        solutions (list of lists): List of solutions,
        each represented as a list of queen positions.
    """
    for solution in solutions:
        print("[", end='')
        for i in range(len(solution)):
            if i > 0:
                print(", ", end='')
            print("[{}, {}]".format(solution[i].index(1), i + 1), end='')
        print("]")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 0-nqueens.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)

