def most_water(containers: list[int]):
    ans = 0
    left = 0
    right = len(containers) - 1
    while left < right:
        _min = min(containers[left], containers[right])
        ans = max(ans, _min * (right - left))
        if containers[left] < containers[right]:
            left += 1
        else:
            right -= 1
    return ans

print(most_water([1,8,6,2,5,4,8,3,7]))