a1 = float(input("первый коэф:"))
b1 = float(input("второй коэф:"))
c1 = float(input("третий коэф:"))
a2 = float(input("первый коэф:"))
b2 = float(input("второй коэф:"))
c2 = float(input("третий коэф:"))
D = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / D
y = (a1 * c2 - a2 * c1) / D 
print(f"X: {x}")
print(f"Y: {y}")