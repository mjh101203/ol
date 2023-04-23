N, M = map(int, input().split())
l = list(range(1, N+1))
O = []
for i in range(0, M):
    i, j = map(int, input().split())
    O = l[i-1:j]
    O.reverse()
    l[i-1:j] = O
print(*l)