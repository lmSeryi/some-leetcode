def max_subarray(nums):
    curr = nums[0]
    _max = nums[0]
    for i in range(len(nums)):
        curr = max(nums[i], nums[i] + curr)
        _max = max(_max, curr)

    return max

print(max_subarray([]))