class WordleBoard:
    def __init__(self):
        self.board = [[],[],[],[],[]]
        self.word = "abort"

    def printBoard(self):
        boardString = ''
        for line in self.board:
            for letter in line:
                boardString += letter
            boardString += "\n"
        print(boardString)

    def takeGuess(self):
        resp = input("Please enter a guess:\n")
        self.board[0] = list(resp)

board = WordleBoard()

board.printBoard()