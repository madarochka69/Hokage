N = int(input("Введите N: "))
s = 1
p = 1
q = 2
while p < N:
    s, p = p, s + p
    q += 1
print(q)