def climbing_stairs(n: int):
    if n <= 2:
        return n

    first, second = 1, 2

    for _ in range(1, n - 2):
        temp = first + second
        first = second
        second = temp
    
    return second


print(climbing_stairs(6))
