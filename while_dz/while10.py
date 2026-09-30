N = int(input("Введите N: "))
q = 0
p = 1
while p < N:
    p *= 3
    q += 1
print(q - 1)