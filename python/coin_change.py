def coin_change(coins: list[int], amount):
    dp = [0] * (amount + 1)

    for i in range(1, amount + 1):
        _min = float("inf")
        for coin in coins:
            if i >= coin and dp[i - coin] != -1:
                _min = min(_min, dp[i - coin])

        dp[i] = -1 if _min == float("inf") else 1 + _min

    return dp[-1]

print(coin_change([1,2,5], 11))
