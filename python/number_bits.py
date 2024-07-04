def counting_bits(n: int):
    dp = [0] * (n + 1)
    offset = 2

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp

print(counting_bits(0))