a = int(input())
def fib(n):
    d = {
        1: 1,
        2: 1
    }
    count = 0
    for i in range(3, n+1):
        count += 1
        d[i] = d[i - 1] + d[i - 2]
    return d[n], count
print(*fib(a))