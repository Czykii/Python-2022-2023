import itertools
import random
  
def a():
    iter_a = itertools.cycle([0,1])

    for i in range(15):
        print(next(iter_a), end = ", ")

def b():
    iter_b = iter(lambda: random.choice(["N","E","S","W"]), 1)

    for i in range(15):
        print(next(iter_b), end = ", ")


def c():
    iter_c = itertools.cycle([0,1,2,3,4,5,6])

    for i in range(15):
        print(next(iter_c), end = ", ")


if __name__ == "__main__":
    a()
    print()
    b()
    print()
    c()
    print()