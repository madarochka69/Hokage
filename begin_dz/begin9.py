a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))
sg = (a * b) ** 0.5
if a <= 0:
    print(False)
elif b <= 0:
    print(False)
else:
    print(f"Среднее геометрическое = {sg}")