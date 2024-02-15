#!/usr/bin/python3

def prime_generator():
    """
    Generates an infinite stream of prime numbers using a generator.

    Yields:
        int: Prime numbers.
    """
    yield 2  # Start with the first prime number
    primes = [2]  # Keep track of discovered prime numbers
    num = 3  # Start checking from the next odd number

    while True:
        is_prime = all(num % p != 0 for p in primes)
        if is_prime:
            primes.append(num)
            yield num
        num += 2  # Move to the next odd number

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List of integers representing the set of numbers for each round.

    Returns:
        str or None: Name of the player who won the most rounds (either "Maria" or "Ben").
                     If the winner cannot be determined, returns None.
    """
    prime_gen = prime_generator()
    maria_wins = 0

    for _ in range(x):
        maria_turn = True
        for _ in range(nums[_]):
            next_prime = next(prime_gen)
            if next_prime > nums[_]:
                break
            maria_turn = not maria_turn

        if maria_turn:
            maria_wins += 1

    if maria_wins > x // 2:
        return "Maria"
    elif maria_wins < x // 2:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))

