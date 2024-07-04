def minimum_sorted(nums: list[int]):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    if nums[0] < nums[len(nums) - 1]:
        return nums[0]

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid+1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[left] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

print(minimum_sorted([6,7,8,9,0, 1,2,3,4,5]))