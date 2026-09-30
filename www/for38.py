N = int(input("Введите N: "))
s = 0.0
for q in range(1, N + 1):
    px = 1.0
    for j in range(1, N - q + 2):
        px *= q
    s += px
print(s)
