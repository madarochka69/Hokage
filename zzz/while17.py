N = int(input("Введите N: "))
while N > 0:
    digit = N % 10
    print(digit)
    N //= 10