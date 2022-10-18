with open('line.txt', 'r') as file:
    line = file.read()
words = line.lower().split()

words_sorted = sorted(words)
print(words_sorted)
print()
words_length = sorted(words, key=len)
print(words_length)