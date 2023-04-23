a = str(input())
b = int(a)
i = 0
while i < b:
    for i in range(1, b + 1):
        n = sum(map(int,str(i)))
        if i + n == b:
            print(i)
            break
    break
print(0)

# or

# a = int(input())
# i = 0
# b = 0
# for i in range(1, a+1):
#     n = sum(map(int,str(i)))
#     if i + n == a:
#         b = i
#         break

# print(b)