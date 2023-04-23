a = int(input())
s = set()
for _ in range(a):
    s.add(input())
l = list(s)
l.sort(key = lambda x : [len(x),x])
print(*l, sep="\n")