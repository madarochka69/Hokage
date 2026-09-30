N = int(input("Введите N: "))
s = 1
p = 2
w = 3
print(s)
if N > 1:
    print(p)
if N > 2:
    print(w)
for q in range(4, N + 1):
    s, p, w = p, w, w + p - 2 * s
    print(w)
