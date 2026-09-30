N = int(input("Введите N: "))
q = 0
while N > 1:
    div = 0
    while N >= 2:
        N -= 2
        div += 1
    N = div
    q += 1
print(q)