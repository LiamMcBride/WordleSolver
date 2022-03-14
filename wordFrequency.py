from master import wordList, frequencyList

fileName = wordList

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "y",
    "x",
    "z"
    ]
scores = [0] * 26

with open(fileName) as f:
    lines = f.readlines()
    for i in range(0, len(letters)):
        temp = 0
        for line in lines:
            if letters[i] in line[0:-1]:
                temp += 1
        scores[i] = temp / len(lines)
f.close()

for i in range(0, len(letters)):
    print(str(scores[i] * 100))

with open(frequencyList, "w") as f:
    for i in range(0, len(scores)):
        f.write(str(scores[i] * 100) + "\n")
f.close()
