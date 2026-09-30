a = float(input("Введите значение угла в радианах: "))
p = 3.14
if 0 < a < 2 * p:
    grad = a * 180 / p
    print(f"в градусах = {grad}")
else:
        print(False) 