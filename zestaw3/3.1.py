x = 2; y = 3;
if (x > y):
    result = x;                                 #błędem są powtarzające się znaki ";"
else:
    result = y;

for i in "axby": if ord(i) < 100: print (i)     #if powinien być w nowej linijce i po tabulacji

for i in "axby": print (ord(i) if ord(i) < 100 else i)