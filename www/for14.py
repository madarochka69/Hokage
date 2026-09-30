N = int(input("Введите N: "))
s = 0 
for q in range(1, 2 * N, 2):
    s += q
    print(s)