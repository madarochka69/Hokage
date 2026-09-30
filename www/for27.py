X = float(input("Введите X: "))
N = int(input("Введите N: "))
s = X
px = X 
w = 1
for q in range(1, N + 1):
    px *= (X * X)
    w *= (2 * q - 1) / (2 * q)
    s += w * (px / (2 * q + 1))
print(s)