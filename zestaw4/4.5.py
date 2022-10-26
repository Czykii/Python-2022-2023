def odwracanie_it(L, left, right):
    L_new = ''
    for i in range(0, left):
        L_new = L_new + L[i]

    for i in range(right, left - 1, -1):
        L_new = L_new +  L[i]
    
    for i in range(right + 1, len(L)):
        L_new = L_new + L[i]

    return L_new

def odwracanie_rek(L, left, right):     #do zrobienia
    L


L = '12345678'
print(odwracanie_it(L, 0, 6))