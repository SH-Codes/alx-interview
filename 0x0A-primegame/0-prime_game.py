def isWinner(x, nums):
    def sieve(n):
        primes = []
        is_prime = [True] * (n + 1)
        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
        return primes

    def play_game(n):
        primes = sieve(n)
        moves = 0
        while primes:
            prime = primes.pop(0)
            moves += 1
            primes = [p for p in primes if p % prime != 0]
        return moves % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
