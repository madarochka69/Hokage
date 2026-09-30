A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
q = 0
ca = A
while ca >= C:
    cb = B
    while cb >= C:
        q += 1
        cb -= C
    ca -= C
print(q)