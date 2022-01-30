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
        #["o","o","o","x","o"]

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

let = Letter("a", ["O","O","X","O","O"])
let2 = Letter("e", ["O","O","X","O","O"])

temp = "cleat"

print(let.match(temp) and let2.match(temp))

print(let.score)
let.updateScore(["O","X","O","O","O"])
print(let.score)