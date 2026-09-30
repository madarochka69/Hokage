N = int(input("Введите N: "))
s = 0
q = 0
while N > 0:
    digit = N % 10
    s += digit
    q += 1
    N //= 10
print(q)
print(s)