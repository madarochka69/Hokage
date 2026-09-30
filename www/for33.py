N = int(input("Введите N: "))
s = 1
p = 1
print(s)
if N > 1:
    print(p)
for q in range(3, N + 1):
    s, p = p, s + p
    print(p)