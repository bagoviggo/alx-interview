#!/usr/bin/python3
def check_prime(n):
    """
    Check if a given number n is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def add_prime(n, primes):
    """
    Add prime numbers up to n to the list of primes.

    Args:
        n (int): The maximum value up to which to find primes.
        primes (list[int]): List of known prime numbers.

    Returns:
        None
    """
    last_prime = primes[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if check_prime(i):
                primes.append(i)
            else:
                primes.append(0)

def isWinner(x, nums):
    """
    Determine the winner for each round of the game.

    Args:
        x (int): Number of rounds.
        nums (list[int]): Array of n for each round.

    Returns:
        str or None: Name of the player that won the most rounds.
                     If the winner cannot be determined, returns None.
    """
    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]  # Initialize with known primes (0 for non-primes)
    add_prime(max(nums), primes)  # Precompute primes up to the maximum n

    for round in range(x):
        # Calculate the sum of primes less than or equal to nums[round]
        prime_count = sum((i != 0 and i <= nums[round]) for i in primes[:nums[round] + 1])
        if prime_count % 2:
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    # Compare scores and determine the overall winner
    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"
    else:
        return None  # Cannot determine a winner
