X = float(input("Введите X: "))
N = int(input("Введите N: "))
s = 1.0 + X / 2.0
px = X
w = 0.5
si = 1
for q in range(2, N + 1):
    si *= -1
    px *= X
    w *= (2 * q - 3) / (2 * q)
    s += si * w * px
print(s)