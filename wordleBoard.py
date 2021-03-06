import os
import random

class WordleBoard:
    def __init__(self):
        self.board = [
            ["-","-","-","-","-"],
            ["-","-","-","-","-"],
            ["-","-","-","-","-"],
            ["-","-","-","-","-"],
            ["-","-","-","-","-"],
            ["-","-","-","-","-"]
            ]
        self.scoreBoard = [
            ["i","i","i","i","i"],
            ["i","i","i","i","i"],
            ["i","i","i","i","i"],
            ["i","i","i","i","i"],
            ["i","i","i","i","i"],
            ["i","i","i","i","i"]
            ]
        self.bank = [
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
        #self.word = self.getWord()
        self.word = "cares"
        self.guess = 0

    def printBoard(self):
        boardString = ''
        for i in range(0,6):
            for letter in self.board[i]:
                boardString += letter
            boardString += "\n"
            for letter in self.scoreBoard[i]:
                boardString += letter
            boardString += "\n"
        print(boardString)

    def takeGuess(self, resp):
        # resp = input("Please enter a guess:\n")
        if self.checkInBank(resp):
            self.board[self.guess] = list(resp)
            self.guess += 1
        else:
            print("Not a word")
            self.takeGuess(input("Please enter a guess:\n"))
    
    def checkInBank(self, word):
        words = []        
        with open('cleanDict.txt') as f:
            lines = f.readlines()
            for line in lines:
                words.append(line[0:-1])
        f.close()
        return word in words

    def verifyGuess(self):
        # if(self.word == self.createWord()):
        #     print("correct")
        # else:
        for i in range(0,5):
            let = self.board[self.guess - 1][i]
            if let == self.word[i]:
                self.scoreBoard[self.guess - 1][i] = "C"
            elif let in self.word:
                self.scoreBoard[self.guess - 1][i] = "O"
            else:
                self.scoreBoard[self.guess - 1][i] = "X"
                if let in self.bank:
                    self.bank.remove(let)
                

    def createWord(self):
        word = ""
        for let in self.board[self.guess - 1]:
            word += let
        return word

    def getWord(self):
        words = []
        with open('cleanDict.txt') as f:
            words = f.readlines()
        f.close()

        word = random.choice(words)

        return word[0:-1]

    def showWordBank(self):
        line = "\n\n"
        for let in self.bank:
            line += let + " "
        print(line)



board = WordleBoard()
for i in range(0,6):
    board.takeGuess(input("Please enter a guess:\n"))
    board.verifyGuess()
    os.system('cls')
    board.printBoard()
    board.showWordBank()

print(board.word)

