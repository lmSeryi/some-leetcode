def reverse_bits(n: int):
    reverse = 0
    for i in range(33):
        reverse = reverse << 1
        reverse = reverse | (1 & n)
        n = n >> 1

    return reverse
