N = int(input("Введите N: "))
s = 1
p = 1
for q in range(1, N + 1):
    p *= q          
    s += 1 / p    
print(s)
