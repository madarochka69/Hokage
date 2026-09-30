a = float(input("первый коэф:"))
b = float(input("второй коэф:"))
c = float(input("третий коэф:"))
D = b ** 2 - 4 * a * c
if a != 0 and D > 0:
    x1 = (-b - (D ** 0.5)) / (2 * a)
    x2 = (-b + (D ** 0.5)) / (2 * a)
    if x1 < x2:
        print(f"Меньший корень: {x1}")
        print(f"Больший корень: {x2}")
    else:
        print(f"Меньший корень: {x2}")
        print(f"Больший корень: {x1}")
else: 
    print(False)             