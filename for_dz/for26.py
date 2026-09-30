X = float(input("Введите X: "))
N = int(input("Введите N: "))
s = X
px = X 
si = 1
for q in range(1, N + 1):
    si *= -1
    px *= (X * X)
    s += si * (px / (2 * q + 1))
print(s)
