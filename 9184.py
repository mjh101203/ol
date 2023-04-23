def memo(f):
    cache = {}

    def helper(a, b, c):
        if (a, b, c) not in cache:
            cache[(a, b, c)] = f(a, b, c)
        return cache[(a, b, c)]
    return helper


@memo
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


w(10, 10, 10)