N = int(input("Введите N: "))
s = 1.0
while N > 0:
    s *= N
    N -= 2
print(s)