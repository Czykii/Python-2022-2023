L = [[],[4],(1,2),[3,4],(5,6,7)]
L_new = []

print(L)
for i in range(0, len(L)):
    summ = 0
    for j in range(0, len(L[i])):
        summ = summ + L[i][j]
    L_new.append(summ)
print(L_new)
