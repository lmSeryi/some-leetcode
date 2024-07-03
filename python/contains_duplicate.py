def contains_duplicate(arr: list[int]):
    _dict = dict()

    for num in arr:
        if num in _dict:
            return True
        _dict[num] = False

    return False

print(contains_duplicate([1,2,3,4,5, 1]))