# Zestaw 10

##### OBOWIĄZKOWE DO PRZESŁANIA: jedno zadanie ze stosem lub kolejką (10.2 - 10.7), zadanie z kolejką przypadkową (10.8)

## Zadanie 10.4 (QUEUE)
Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek. Poprawić metodę put() w tablicowej implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek. Napisać kod testujący kolejkę.


## Zadanie 10.8 (RANDOMQUEUE)
Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.

``` python
class RandomQueue:

    def __init__(self): pass
    #def __init__(self, size=10): pass   # wersja z ograniczeniem na rozmiar

    def insert(self, item): pass   # wstawia element w czasie O(1)

    def remove(self): pass   # zwraca losowy element w czasie O(1)

    def is_empty(self): pass

    def is_full(self): pass

    def clear(self): pass   # czyszczenie listy
```