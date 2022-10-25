ruler = ''

length = int(input('Jak długa ma być linijka? '))

for i in range(0, length):
    ruler = ruler + '|....'

ruler = ruler + '|'

ruler = ruler + '\n'
for k in range(0, length):
    ruler = ruler + str(k) + (' ' * (5 - len(str(k))))
    
ruler = ruler + str(length)

print(ruler)
