N = int(input("N = "))
p = 1.0
s = 0.0
for q in range(1, N + 1):
    p *= q
    s += p
print("Сумма:", s)