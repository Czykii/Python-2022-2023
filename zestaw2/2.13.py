with open('line.txt', 'r') as file:
    line = file.read()

words = line.split()
lengths = [len(word) for word in words]

print('Długość słów:', sum(lengths))
