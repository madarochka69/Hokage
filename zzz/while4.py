N = int(input("Введите N: "))
ir = True
if N <= 0:
    ir = False
while N > 1 and ir:
    q = 0
    while N >= 3:
        N -= 3
        q += 1
    if N != 0:
        ir = False
    N = q
print(ir)