a = int(input())
d = list(map(int, input().split()))
e = int(input())
c = 0
for i in d:
    if i == e :
        c += 1
print(c)