position = input("Enter the position: ")
column = position[0]
row = int(position[1])
column_indices = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
column_number = column_indices[column]
sum_indices = column_number + row
if sum_indices % 2 == 0:
    print("The square is black.")
else:
    print("The square is white.")