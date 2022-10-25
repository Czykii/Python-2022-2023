x = 2; y = 3;
if (x > y):
    result = x;                                 #to nie jest błąd
else:
    result = y;

for i in "axby": if ord(i) < 100: print (i)     #To jest błąd, ponieważ              (if powinien być w nowej linijce i po tabulacji)

for i in "axby": print (ord(i) if ord(i) < 100 else i)      #to nie jest błąd