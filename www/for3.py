A = int(input("Введите A: "))
B = int(input("Введите B: "))
k = 0
for q in range(B - 1, A, -1):
    print(q)
    k +=1
print("Количество чисел:", k)