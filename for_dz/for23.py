X = float(input("Введите X: "))
N = int(input("Введите N: "))
s = X
p = 1
px = X 
si = 1
for q in range(1, N + 1):
    si *= -1
    px *= (X * X)
    p *= (2 * q) * (2 * q + 1)
    s += si * (px / p)
print(s)