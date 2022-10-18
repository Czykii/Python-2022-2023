L = [1, 34, 22, 56, 321, 37]
L_string = [str(x) for x in L]

for i in range(0, len(L_string)):
    L_string[i] = L_string[i].zfill(3)
    i = i + 1

print(L_string)