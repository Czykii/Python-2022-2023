def roman2int(string):
    roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    intig = 0

    for i in range(len(string)):
        if i > 0 and roman[string[i]] > roman[string[i - 1]]:
            intig += roman[string[i]] - 2 * roman[string[i - 1]]
        else:
            intig += roman[string[i]]
    
    return intig

print('MMXXIII')
print(roman2int('MMXXIII'))
print()
print('CMXLIX')
print(roman2int('CMXLIX'))

'''
słownik można również zrobić tak:

roman = {}
roman['I'] = 1
roman['V'] = 5
roman['X'] = 10
roman['L'] = 50
roman['C'] = 100
roman['D'] = 500
roman['M'] = 1000
'''