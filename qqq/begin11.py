a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))
sum = abs(a) + abs(b)
raz = abs(a) - abs(b)
pro = abs(a) * abs(b)
cha = abs(a) / abs(b)
if a == 0:
    print(False)
elif b == 0:
    print(False)
else:
    print(f"Сумма модулей = {sum}")
    print(f"Разность модулей = {raz}")
    print(f"Произведение модулей = {pro}")
    print(f"Частное модулей = {cha}")