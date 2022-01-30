words = []
lines = []

with open('wordDictionary.txt') as f:
    lines = f.readlines()
f.close()

for line in lines:
     words.append(line)

words.sort()

print(words)

with open('cleanDict.txt', 'w') as f:
    f.writelines(words)
f.close()