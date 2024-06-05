x = float(input("Input a positive value:"))
y = x/2
while True:
    newy = (y + x/y)/2
    if abs(newy * newy - x) <= 0.001:
        break
    y = newy
print(newy)


