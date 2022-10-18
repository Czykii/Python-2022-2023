word = 'python'

print(word)

letters = list(word)

length = len(letters)

for i in range(0, len(letters)):
    if i != (length - 1):
        print(letters[i] + '_', end='')
    else:
        print(letters[i])    