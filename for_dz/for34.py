N = int(input("Введите N: "))
s = 1.0
p = 2.0
print(s)
if N > 1:
    print(p)
for q in range(3, N + 1):
    s, p = p, (s + 2.0 * p) / 3.0
    print(p)