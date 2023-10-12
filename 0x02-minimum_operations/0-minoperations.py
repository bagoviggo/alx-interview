#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to reach n characters.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to reach n characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations.

    If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
