x=2
a = -1
n = 1387
xi = x
yi = (xi**2 + a) % n
y = 0
xl = 1
for i in range(0, 11):
    xi = (xi**2 + a) % n
    print(xi)
xi = x
for i in range(1,6):
    xi = (xi**2 + a) % n
    y += 1
    while(xl < i*2):
        yi = (yi**2 + a) % n
        xl += 1    
    print(xi, yi)
