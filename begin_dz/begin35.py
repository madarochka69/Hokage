v = float(input("скорость лодки:"))
u = float(input("скорость течения:"))
t1 = float(input("время по течению:"))
t2 = float(input("время против течения:"))
if v > u and t1 >= 0 and t2 >= 0:
    S = v * t1 + (v - u) * t2
    print(f"Общий пройденный путь = {S}")
else:
    print(False)