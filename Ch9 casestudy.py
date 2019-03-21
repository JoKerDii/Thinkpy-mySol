fin = open('words.txt')
print(fin.readline())

line = fin.readline()
word = line.strip()
print(word)

for line in fin:
    word = line.strip()
    print(word)
    