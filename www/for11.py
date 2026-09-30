N = int(input("Введите N: "))
s = 0
for q in range(N, 2 * N + 1):
    s += q ** 2
print(s)