def sum_integers(a: int, b:int):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print(sum_integers(14,10))