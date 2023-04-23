l = list(range(1, 31))
for _ in range(28):
    a = int(input())
    l.remove(a)
print(min(l))
print(max(l))