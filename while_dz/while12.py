N = int(input("Введите N: "))
s = 0
q = 0
while s + (q + 1) <= N:
    q += 1
    s += q
print(q)
print(s)