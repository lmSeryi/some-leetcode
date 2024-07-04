def search_rotated(nums: list[int], k):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == k:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= k < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < k <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print(search_rotated([3,1,2], 3))