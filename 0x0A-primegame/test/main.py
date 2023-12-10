#!/usr/bin/python3
"""Script to test the isWinner function."""

from prime_game import isWinner

# Test case from the challenge
x = 3
nums = [4, 5, 1]
print("Winner:", isWinner(x, nums))  # Expected output: "Ben"

# Additional test cases
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # You can add more test cases


