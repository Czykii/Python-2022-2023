square = ''

wid = int(input('Podaj pierwszy wymiar prostokąta: '))
leng = int(input('Podaj drugi wymiar prostokąta: '))

for i in range(0, wid):
    for j in range(0, leng):
        square = square + '+---'
    square = square + '+' + '\n'

    for k in range(0, leng):
        square = square + '|' + (' ' * 3)
    square = square + '|' + '\n'

for x in range(0, leng):
    square = square + '+---'   
square = square + '+' + '\n'

print(square)