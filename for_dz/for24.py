X = float(input("Введите X: "))
N = int(input("Введите N: "))
s = 1
p = 1
px = 1
si = 1
for q in range(1, N + 1):
    si *= -1
    px *= (X * X)
    p *= (2 * q - 1) * (2 * q)
    s += si * (px / p)
print(s)