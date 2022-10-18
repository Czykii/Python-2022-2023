with open('line.txt', 'r') as file:
    line = file.read()

words = line.split()

print('Napis ma' , len(words) , 'słów')