def odwracanie_it(L, left, right):
    stop = (right - left) // 2
    for i in range(stop):
        L[left], L[right] = L[right], L[left]
        left = left + 1
        right = right - 1
    return L

def odwracanie_rek(L, left, right):     #do zrobienia
    if left+1 != right and left != right:
        L[left], L[right] = L[right], L[left]
        return odwracanie_rek(L, left+1, right-1)
    else:
        return L


L = [x for x in range(1, 9)]
print(L)
print(odwracanie_it(L, 1, 6))

L2 = [x for x in range(1, 9)]
print(odwracanie_rek(L2, 1, 6))