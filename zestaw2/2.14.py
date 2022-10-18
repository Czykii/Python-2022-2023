with open('line.txt', 'r') as file:
    line = file.read()
words = line.split()

maks = 0
indeks = 0
for i in range(0, len(words)):
    if len(words[indeks]) < len(words[i]):
        indeks = i
        maks = len(words[i])
    i = i + 1
print('Najdłuższe słowo:', words[indeks])
print('Długość słowa:', maks)