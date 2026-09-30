A = float(input("Введите A: "))
B = float(input("Введите B: "))
q = 0
while A >= B:
    A -= B
    q += 1
print(q)