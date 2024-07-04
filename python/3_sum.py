def my_sum(nums: list[int]):
    nums = sorted(nums)
    my_list = []

    for i in range(0, len(nums) - 2):
        if i == 0 or nums[i] != nums[i - 1]:
            left = i + 1
            right = len(nums) - 1
            target = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    triplets = [nums[i], nums[left], nums[right]]
                    my_list.append(triplets)
                    while nums[left] == nums[left + 1]:
                        left += 1
                    while nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
    return my_list


print(my_sum([-2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2]))
