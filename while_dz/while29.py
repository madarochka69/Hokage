eps = float(input("Введите eps: "))
s = 1
p = 2
q = 2
while True:
    w = (s + 2 * p) / 3
    q += 1
    if abs(w - p) < eps:
        break
    s, p = p, w
print(q)
print(p)
print(w)