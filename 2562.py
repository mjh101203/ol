a = int(input())
c = 0
for i in range(1, 9):
    b = int(input())
    if a > b :
        a = int(a)
        c = i
    else :
        a = int(b)
        c = i-1
print(a)
print(c)