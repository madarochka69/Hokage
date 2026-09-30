eps = float(input("Введите eps: "))
s = 2
q = 1
while True:
    p = 2 + 1 / s
    q += 1
    if abs(p - s) < eps:
        break
    s = p
print(q)
print(s)
print(p)