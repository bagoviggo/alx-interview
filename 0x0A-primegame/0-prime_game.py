#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List of integers representing
        the set of numbers for each round.

    Returns:
        str or None: Name of the player who won the most rounds
        (either "Maria" or "Ben").
                     If the winner cannot be determined, returns None.
    """
    def is_prime(num):
        """
        Checks if a given number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(nums, start):
        """
        Finds the next prime number in the list.

        Args:
            nums (List[int]): List of integers.
            start (int): Index to start searching from.

        Returns:
            int or None: Next prime number or None if not found.
        """
        for num in nums[start:]:
            if is_prime(num):
                return num
        return None

    def play_round(nums):
        """
        Simulates a single round of the game.

        Args:
            nums (List[int]): List of integers for the current round.

        Returns:
            bool: True if Maria wins the round, False if Ben wins.
        """
        maria_turn = True
        while nums:
            next_prime = get_next_prime(nums, 0)
            if next_prime is None:
                break
            nums.remove(next_prime)
            maria_turn = not maria_turn
        return maria_turn

    maria_wins = 0
    for _ in range(x):
        if play_round(nums.copy()):
            maria_wins += 1

    if maria_wins > x // 2:
        return "Maria"
    elif maria_wins < x // 2:
        return "Ben"
    else:
        return None
