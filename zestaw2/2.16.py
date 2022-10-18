with open('line.txt', 'r') as file:
    line = file.read()

print(line)
print()
new_line = line.replace("GvR", "Guido van Rossum")
print(new_line)