A = float(input("Введите A: "))
s = 0
q = 0
while s + 1 / (q + 1) < A:
    q += 1
    s += 1 / q
print(q)
print(s)