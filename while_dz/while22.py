N = int(input("Введите N: "))
ir = True
q = 2
while q * q <= N:
    if N % q == 0:
        ir = False
    q += 1
print(ir)