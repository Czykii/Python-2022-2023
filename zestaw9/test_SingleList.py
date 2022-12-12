from SingleList import SingleList, Node

def test_remove_tail():
    lista = SingleList()
    lista.insert_tail(Node(1))
    lista.insert_tail(Node(2))
    lista.insert_tail(Node(3))
    assert lista.remove_tail().data == 3
    assert lista.remove_tail().data == 2
    assert lista.remove_tail().data == 1
    assert lista.count() == 0

def test_join():
    lista = SingleList()
    lista.insert_tail(Node(1))
    lista.insert_tail(Node(2))
    lista.insert_tail(Node(3))
    lista2 = SingleList()
    lista2.insert_tail(Node(4))
    lista2.insert_tail(Node(5))
    lista2.insert_tail(Node(6))
    lista.join(lista2)
    assert lista2.count() == 0
    for i in range(1, 7):
        assert lista.remove_head().data == i

def test_clear():
    lista = SingleList()
    lista.insert_tail(Node(1))
    lista.insert_tail(Node(2))
    lista.clear()
    assert lista.head is None
    assert lista.tail is None
    assert lista.count() == 0