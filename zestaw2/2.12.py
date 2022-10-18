with open('line.txt', 'r') as file:
    line = file.read()

words = line.split()

print("Słowo z pierwszych liter:")
for i in range(0,len(words)):
    print(words[i][0], end='')
print()

print("Słowo z pierwszych liter:")
for k in range(0,len(words)):
    lenght = len(words[k])
    print(words[k][lenght - 1], end='')
print()
