import math
N = int(input("Введите N: "))
A = float(input("Введите A: "))
B = float(input("Введите B: "))
H = (B - A) / N
print("Длина H:", H)
for q in range(0, N + 1):
    x = A + q * H
    f = 1 - math.sin(x)
    print(f)