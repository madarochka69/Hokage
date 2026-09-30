N = int(input("Введите N: "))
s = 1.0
for q in range(1, N + 1):
    s = (s + 1.0) / q
    print(s)