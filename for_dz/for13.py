N = int(input("Введите N: "))
s = 0 
for q in range(1, N + 1):
    s += (1 + q / 10) * (-1) ** (q + 1)
print(s)