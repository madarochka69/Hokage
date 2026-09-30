N = int(input("Введите N: "))
s = 1
p = 1
while p <= N:
    s, p = p, s + p
print(p)