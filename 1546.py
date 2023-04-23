a = int(input())
l = list(map(int, input().split()))
n = max(l)
c = 0
for i in range(0, a):
    c += (l[i]/n*100)
print(c/a)