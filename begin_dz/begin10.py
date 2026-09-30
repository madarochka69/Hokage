a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))
sum = a ** 2 + b ** 2
raz = a ** 2 - b ** 2
pro = a ** 2 * b ** 2
cha = a ** 2 / b ** 2
if a == 0:
    print(False)
elif b == 0:
    print(False)
else:
    print(f"Сумма корней = {sum}")
    print(f"Разность корней = {raz}")
    print(f"Произведение корней = {pro}")
    print(f"Частное корней = {cha}")