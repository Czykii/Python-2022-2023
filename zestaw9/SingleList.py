class Node:
    """Klasa reprezentujaca wezel listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogolnie
class SingleList:
    """Klasa reprezentujaca cala liste jednokierunkowa."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczac za kazdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie lacza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):   # klasy O(n)
        # Zwraca caly wezel, skraca liste.
        # Dla pustej listy rzuca wyjatek ValueError.
        res = self.tail
        if self.length == 0:
            raise ValueError('pusta lista')
        elif self.length == 1:
            self.head = self.tail = None
            self.length = self.length - 1
            return res
        else:
            temp = self.head
            while (temp.next != self.tail):
                temp = temp.next
            
            self.length = self.length - 1
            temp.next = None
            self.tail = temp
            return res

    def join(self, other):   # klasy O(1)
        # Wezly z listy other sa przepinane do listy self na jej koniec.
        # Po zakonczeniu operacji lista other ma byc pusta.
        self.tail.next = other.head
        self.tail = other.tail
        self.length = self.length + other.length
        other.clear()

    def clear(self):   # czyszczenie listy
        self.head = self.tail = None
        self.length = 0