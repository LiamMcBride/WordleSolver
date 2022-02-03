from sympy import false

class LetterHolder:
    def __init__(self):
        self.letters = []
        self.nonValid = []
    
    def addLetter(self, letter):
        if "C" in letter.score or "O" in letter.score:
            exists = False
            for let in self.letters:
                if let.letter == letter.letter:
                    exists = True
                    let.updateScore(letter.score)
            if not exists:
                self.letters.append(letter)
        else:
            self.nonValid.append(letter.letter)
        
        


            

class Letter:
    def __init__(self, letter, score):
        self.letter = letter
        self.score = score
        self.rating = 0
        #["x","x","x","o","o"]

    def setRating(self, newRating):
        self.rating = newRating

    def updateScore(self, newScore):
        #["","","x","",""]
        for i in range(0,5):
            if newScore[i] != self.score[i] and self.score[i] != "X":
                self.score[i] = newScore[i]

    def match(self, word):
        if self.letter in word:
            for i in range(0,5):
                if self.score[i] == "X" and word[i] == self.letter:
                    return False
                elif self.score[i] == "C" and word[i] == self.letter:
                    return True
                elif self.score[i] == "O" and word[i] == self.letter:
                    return True
        else:
            return False

class FrequencyMaker:
    def __init__(self):
        self.letters = [
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
        self.fileName = "frequency.txt"
        self.frequencyDict = {}
        self.create()
    
    def create(self):
        with open(self.fileName) as f:
            lines = f.readlines()
            for line in lines:
                self.frequencyDict[self.letters.pop()] = float(line[0:-1])
        f.close()
        #print(self.frequencyDict)
    
    def score(self, words):
        best = 0
        bestWord = ""

        for word in words:
            lets = list(word)

            temp = 0
            for let in word:
                temp += self.frequencyDict[let]
            
            if temp > best:
                best = temp
                bestWord = word

        return(bestWord)



# let = Letter("a", ["O","O","X","O","O"])
# let2 = Letter("e", ["O","O","X","O","O"])

# temp = "cleat"

# print(let.match(temp) and let2.match(temp))

# print(let.score)
# let.updateScore(["O","X","O","O","O"])
# print(let.score)

f = FrequencyMaker()


#print(f.frequencyDict["s"])

print(f.score(["later","notes","acrid"]))
