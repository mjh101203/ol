n, m = map(int, input().split())
a = 0
l = list(i for i in range(0,6))
for _ in range(m):
    i, j = map(int, input().split())
    a = i
    l[i] = l[j]
    l[j] = l[a]
print(*l[1:])