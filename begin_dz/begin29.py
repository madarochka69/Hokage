a = float(input("Введите значение угла в градусах: "))
p = 3.14
if 0 < a < 360:
    rad = a * p / 180
    print(f"в радианах = {rad}")
else:
    print(False)   