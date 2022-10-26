def make_ruler(n):
    ruler = ''

    for i in range(0, n):
        ruler = ruler + '|....'

    ruler = ruler + '|'

    ruler = ruler + '\n'
    for k in range(0, n):
        ruler = ruler + str(k) + (' ' * (5 - len(str(k))))
    
    ruler = ruler + str(n)
    return ruler

def make_grid(rows, cols):
    square = ''

    for i in range(0, rows):
        for j in range(0, cols):
            square = square + '+---'
        square = square + '+' + '\n'

        for k in range(0, cols):
            square = square + '|' + (' ' * 3)
        square = square + '|' + '\n'

    for x in range(0, cols):
        square = square + '+---'   
    square = square + '+' + '\n'

    return square


print(make_ruler(5))
print()
print(make_grid(2,2))