one = 'shgyemgj572njsfosja'
two = 'nmziutrsl903bulqa'

repeated = ''
unrepeated = ''

for i in range(0, len(one)):
    for j in range(0, len(two)):
        if one[i] == two[j]:
            if not repeated.__contains__(two[j]):
                repeated = repeated + two[j]

print(repeated)

three = one + two

for letter in three:
    if not unrepeated.__contains__(letter):
        unrepeated = unrepeated + letter

print(unrepeated)