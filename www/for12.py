N = int(input("Введите N: "))
p = 1
for q in range(1, N + 1):
    p *= 1 + q / 10
print(p)