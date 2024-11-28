#!/usr/bin/python3

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total.
    If total is 0 or less, return 0.
    If total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0
    if not coins or coins is None:
        return -1

    # Initialize a DP array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
