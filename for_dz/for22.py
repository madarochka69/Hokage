X = float(input("Введите X: "))
N = int(input("Введите N: "))
s = 1
p = 1
px = 1
for q in range(1, N + 1):
    p *= q          
    px *= X 
    s += px / p  
print(s)