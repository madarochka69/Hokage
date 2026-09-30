N = int(input("Введите N: "))
s = 0
while N > 0:
    digit = N % 10
    s = s * 10 + digit
    N //= 10
print(s)