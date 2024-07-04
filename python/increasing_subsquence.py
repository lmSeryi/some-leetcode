def increasing_subsequence(nums: list[int]):
    n = len(nums)
    if n == 1:
        return 1

    dp = [0] * n
    dp[0] = 1

    ans = 0
    for i in range(1, n):
        length = 0
        for j in range(i):
            if nums[j] < nums[i]:
                length = max(length, dp[j])
        dp[i] = 1 + length
        ans = max(ans, dp[i])
    return ans

print(increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
