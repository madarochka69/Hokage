N = int(input("Введите N: "))
K = int(input("Введите K: "))
q = 0
while N >= K:
    N -= K
    q += 1
print(q)
print(N)