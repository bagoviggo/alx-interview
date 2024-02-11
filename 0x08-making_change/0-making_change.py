#!/usr/bin/python3
"""
make_change.py
~~~~~~~~~~~~~~

Module to determine the fewest number of coins needed...
to meet a given amount total.

Functions:
    - makeChange(coins, total):
      Determines the fewest number of coins needed...
      to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
        coins (list of int): The values of the coins in your possession.
        total (int): The amount total to be met.

    Returns:
        int: Fewest number of coins needed to meet total.
        If total is 0 or less, return 0.
        If total cannot be met by any number of coins you have, return -1.

    Example:
        print(makeChange([1, 2, 25], 37))   # Output: 7
        print(makeChange([1256, 54, 48, 16, 102], 1453))   # Output: -1
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
