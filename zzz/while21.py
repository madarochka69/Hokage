N = int(input("Введите N: "))
ir = False
while N > 0:
    d = N % 10
    if d % 2 != 0:
        ir = True
    N //= 10
print(ir)