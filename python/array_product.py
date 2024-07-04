def array_product(nums):
    prefix_product = [0] * len(nums)
    prefix_product[0] = 1
    suffix_product = 1

    for idx in range(1, len(nums)):
        prefix_product[idx] = prefix_product[idx - 1] * nums[idx - 1]

    for i in range(len(nums) - 1, -1, -1):
        prefix_product[i] = prefix_product[i] * suffix_product
        suffix_product = suffix_product * nums[i]

    return prefix_product

print(array_product([1,2,3,4]))