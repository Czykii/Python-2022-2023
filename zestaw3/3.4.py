while True:
    x = input('Podaj liczbę rzeczywistą: ')
    if x == 'stop' or x == 'Stop':
        break
    try:
        number = float(x)
    except:
        print('To nie jest liczba rzeczywista')
        continue
    print(number)
    print(number**3)