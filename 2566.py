l = []
for i in range(9):
    t = list(map(int, input().split()))
    l.append(t)
m = 0
행 = 0
열 = 0
for i in range(9):
    for j in range(9):
        if m <= l[i][j] :
            m = l[i][j]
            행 = i + 1
            열 = j + 1
print(m)
print(행, 열)