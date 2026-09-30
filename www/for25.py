X = float(input("Введите X: "))
N = int(input("Введите N: "))
s = X
px = X 
si = 1
for q in range(2, N + 1):
    si *= -1
    px *= X
    s += si * (px / q)
print(s)