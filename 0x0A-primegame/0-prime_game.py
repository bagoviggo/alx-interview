#!/usr/bin/python3
"""
Module for determining the winner of the prime game.
"""

def isWinner(x, nums):
    """
    Determine the winner of each round and overall winner.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing n for each round.

    Returns:
        str: Name of the player that won the most rounds.
             If the winner cannot be determined, return None.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_next_prime(nums, current):
        for num in nums:
            if num > current and is_prime(num):
                return num
        return None

    def play_round(nums):
        current_player = 'Maria'
        while nums:
            prime = find_next_prime(nums, 0)
            if prime is None:
                break
            nums = [num for num in nums if num % prime != 0]
            current_player = 'Maria' if current_player == 'Ben' else 'Ben'
        return current_player

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(list(range(1, n + 1)))
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("This module is not meant to be executed directly.")

