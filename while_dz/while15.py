P = float(input("Введите P: "))
s = 1000
q = 0
while s <= 1100:
    s += s * P / 100
    q += 1
print(q)
print(s)