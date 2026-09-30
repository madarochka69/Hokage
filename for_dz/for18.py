A = float(input("Введите A: "))
N = int(input("Введите N: "))
p = 1
s = 1
si = -1
for q in range(N):
    p *= A
    s += si * p
    si = -si
print(s)