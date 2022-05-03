def re(n):
    if n < 1:
        return 2
    return (2 * re(n - 1)) + 1

print(re(5))
