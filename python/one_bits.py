def one_bits(n: int):
    count = 0
    for i in range(32):
        mask = 1 << i
        if n & mask != 0:
            count += 1
    return count

print(one_bits(2147483645))