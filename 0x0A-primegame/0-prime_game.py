#!/usr/bin/python3
"""Define isWinner function, a solution to the Prime game
"""


def primes(n):
    """Returns a list of prime numbers between 1 and n inclusive
    Args: n(int): upper boundary of range. lover boundary is always 1"""
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
                return prime


def isWinner(x, nums):
    """Determines the winner of Prime Game
    Agrs: x (int): no. of rounds of the game
    nums(int): upper limit of range for each round
    Return: Name of winner (Maria or Ben) or None if winner cannot be found"""
    # if x is None or nums is None or x == 0 or nums == []:
    #   return None
    # Maria = Ben = 0
    # for i in range(x):
    #   prime = primes(nums[i])
    #  if len(prime) % 2 == 0:
    #     Ben += 1
    # else:
    #   Maria += 1
    #  if Maria > Ben:
    # return 'Maria'
    # elif Ben > Maria:
    #  return 'Ben'
    # return None"""
    if x < 1 or not nums:
        return None
    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for p in range(2, int(max_n**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, max_n + 1, p):
                sieve[multiple] = False
        # Step 2: Precompute the count of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)
        # Step 3: Simulate the game for each round
        maria_wins = 0
        ben_wins = 0
        for n in nums:
            if prime_count[n] % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1
        # Step 4: Determine the overall winner
        if maria_wins > ben_wins:
            return "Maria"
        elif ben_wins > maria_wins:
            return "Ben"
        else:
            return None
