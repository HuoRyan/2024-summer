x = float(input("Input a positive value:"))
y = x/2
newy = y
while abs(newy * newy - x) > 0.001:
    newy = (newy + x/newy)/2

    
print(newy)


