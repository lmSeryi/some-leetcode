def max_product(nums: list[int]):
    ans = nums[0]
    _max = _min = 1
    
    for num in nums:
        if num == 0:
            _min = 1
            _max = 1
            _ans = max(ans, num)
        else:
            temp = _min
            _min = min(num, min(num * _min, num * _max))
            _max = max(num, max(num * temp, num * _max))
            ans = max(ans, _max)
        
    return ans

print(max_product([-1, -2, -3, 0, 3, 5, -1, -2]))