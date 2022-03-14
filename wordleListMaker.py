from master import wordList

words = []
lines = []

with open(wordList) as f:
    lines = f.readlines()
f.close()

for line in lines:
     words.append(line)

words.sort()

print(words)

with open(wordList, 'w') as f:
    f.writelines(words)
f.close()