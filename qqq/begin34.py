x = float(input("кг шоколадных x:"))
a = float(input("стоимость шоколадных a:"))
y = float(input("кг ирисок y:"))
b = float(input("стоимость ирисок b:"))
choc = a / x
iris = b / y
if choc > iris:
    raz = choc / iris
    print(f"1 кг шоколадных = {choc}")
    print(f"1 кг ирисок = {iris}")
    print(f"Разница = {raz}")
else:
    print(False) 