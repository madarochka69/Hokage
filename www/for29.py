N = int(input("Введите N: "))
A = float(input("Введите A: "))
B = float(input("Введите B: "))
H = (B - A) / N
print("Длина H:", H)
for q in range(0, N + 1):
    point = A + q * H
    print(point)
