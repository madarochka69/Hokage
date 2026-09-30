N = int(input("Введите N: "))
ir = False
while N > 0:
    digit = N % 10
    if digit == 2:
        ir = True
    N //= 10
print(ir)