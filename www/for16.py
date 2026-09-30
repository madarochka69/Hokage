A = float(input("Введите A: "))
N = int(input("Введите N: "))
p = 1
for q in range(1, N + 1):
    p *= A
    print(p)