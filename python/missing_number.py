def missing_number(nums: list[int]):
    missing = len(nums)

    for i in range(len(nums)):
        missing ^= nums[i] ^ i


    return missing

print(missing_number([0,1,2,4,5,6]))