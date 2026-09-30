P = float(input("Введите P: "))
s = 10
current_run = 10
q = 1
while s <= 200:
    current_run += current_run * P / 100
    s += current_run
    q += 1
print(q)
print(s)