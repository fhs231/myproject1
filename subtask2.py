n = 0
s = 0
m = float('inf')  

while True:
    
    x = int(input("Enter a natural number (or -1 to finish): "))

    if x == -1:
        break


    n += 1
    s += x
    m = min(m, x)

if n == 0:
    m = -1
    a = -1
else:
    a = s / n

print(f"\nn = {n}, s = {s}, m = {m}, a = {a}")
