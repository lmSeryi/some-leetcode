def two_sum(arr: list[int], target: int):
    _dict = dict()
    resp = [0,0]
    for idx in range(len(arr)):
        complement = target - arr[idx]
        if complement in _dict:
            resp[0], resp[1] = _dict[complement], idx
            return resp
        else:
            _dict[arr[idx]] = idx

print(two_sum([2,1,4,6,7,9,8], 10))