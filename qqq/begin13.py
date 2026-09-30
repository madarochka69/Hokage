r1 = float(input("Введите первый радиус:"))
r2 = float(input("Введите второй радиус:"))
p = 3.14
if r1 < r2:
    print(False)
else:
 s1 = p * r1 ** 2
 s2 = p * r2 ** 2
 s3 = s1 - s2
 print(f'Площадь первого круга = {s1}')
 print(f'Площадь второго круга = {s2}')
 print(f'Площадь кольца = {s3}')