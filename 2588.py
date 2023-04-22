a = int(input())
b = int(input())
c = b%10
d = b%100-c
print(a*c)
print(a*d)
print(a*(b-d))
print(a*b)