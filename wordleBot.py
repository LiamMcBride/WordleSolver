from wordleBoardForBot import WordleBoard as WB
from letter import FrequencyMaker, Letter, LetterHolder
from master import wordList, numRuns, randomGuess
import random

def narrowWords(words, letters):
    newWords = []
    for i in range(0, len(letters.nonValid)):

        for j in range(0, len(words)):
            if not letters.nonValid[i] in words[j]:
                newWords.append(words[j])
        words = newWords
        newWords = []
    print("Words Left:")
    print(len(words))

    for i in range(0, len(letters.letters)):
        for j in range(0, len(words)):
            if letters.letters[i].match(words[j]):
                newWords.append(words[j])
        words = newWords
        newWords = []
    
    print("Words Left:")
    print(len(words))
    return words

def bestLetter(words, letters):
    freq = FrequencyMaker()




def guess(board,words,letters, fails, failed):
    if(len(words) == 0):
        print("------------- Failed --------------")
        if failed == False:
            fails += 1
            failed = True
        # print(board.word)
        # for let in letters.letters:
        #     print(let.letter)
        return board, letters, fails, failed
    
    else:
        newGuess = "soare"
        if(randomGuess):
            newGuess = random.choice(words)
        else:
            freq = FrequencyMaker()

            newGuess = freq.score(words)
        print("Guess is " + newGuess)

        board.takeGuess(newGuess)
        board.verifyGuess()
        board.printBoard()
        board.showWordBank()

        results = board.getScore()[board.guess - 1]

        letterResults = scoreConvert(newGuess, results)
        for i in range(0,5):
            letters.addLetter(Letter(newGuess[i], letterResults[i]))
            
        return board,letters, fails, failed

def scoreConvert(word, score):
    letArr = list(word)
    #soare
    #['C', 'X', 'X', 'X', 'O']
    scores = []

    for i in range(0,5):
        if score[i] != "X":
            if score[i] == "O":
                temp = []
                for j in range(0,5):
                    if j == i:
                        temp.append("X")
                    else:
                        temp.append("O")
                scores.append(temp)
            if score[i] == "C":
                temp = []
                for j in range(0,5):
                    if j == i:
                        temp.append("C")
                    else:
                        temp.append("X")
                scores.append(temp)
        else:
            scores.append(["X","X","X","X","X"])
    return scores

wins = 0
losses = 0
fails = 0
failed = False

for z in range(0, numRuns):

    board = WB()
    freq = FrequencyMaker()


    letters = LetterHolder()
    words = []        
    with open(wordList) as f:
        lines = f.readlines()
        for line in lines:
            words.append(line[0:-1])
    f.close()







    print("------------ First Guess ------------")

    firstGuess = "soare"
    board.takeGuess(firstGuess)
    board.verifyGuess()
    # board.printBoard()
    # board.showWordBank()

    results = board.getScore()[board.guess - 1]

    temp = list(firstGuess)
    letterResults = scoreConvert(firstGuess, results)


    for i in range(0,5):
        letters.addLetter(Letter(firstGuess[i], letterResults[i]))

    secondGuess = ''
    # newWords = []
    # print(letters.nonValid)
    # print(len(letters.letters))
    # for i in range(0, len(letters.nonValid)):

    #     for j in range(0, len(words)):
    #         if not letters.nonValid[i] in words[j]:
    #             newWords.append(words[j])
    #     words = newWords
    #     newWords = []

    # print(len(words))

    # for i in range(0, len(letters.letters)):
    #     for j in range(0, len(words)):
    #         if letters.letters[i].match(words[j]):
    #             newWords.append(words[j])
    #     words = newWords
    #     newWords = []


    # print(len(words))

    words = narrowWords(words, letters)
    print("------------ Second Guess ------------")
    board, letters, fails, failed = guess(board, words, letters, fails, failed)

    # secondGuess = random.choice(words)
    # print("Second guess is " + secondGuess)

    # board.takeGuess(secondGuess)
    # board.verifyGuess()
    # board.printBoard()
    # board.showWordBank()

    # results = board.getScore()[board.guess - 1]
    # print(results)

    # letterResults = scoreConvert(secondGuess, results)
    # print("Letter Results")
    # print(letterResults)
    # for i in range(0,5):
    #     letters.addLetter(Letter(secondGuess[i], letterResults[i]))

    words = narrowWords(words, letters)
    print("------------ Third Guess ------------")
    board, letters, fails, failed = guess(board, words, letters, fails, failed)

    words = narrowWords(words, letters)
    print("------------ Fourth Guess ------------")
    board, letters, fails, failed = guess(board, words, letters, fails, failed)

    words = narrowWords(words, letters)
    print("------------ Fifth Guess ------------")
    board, letters, fails, failed = guess(board, words, letters, fails, failed)

    words = narrowWords(words, letters)
    print("------------ Sixth Guess ------------")
    board, letters, fails, failed = guess(board, words, letters, fails, failed)








# Code fails when there is a double letter word. for shirr a guess of shirr will create a cccco pattern






    print(board.word)

    if board.won:
        wins += 1
    else:
        losses += 1

    failed = False



print("Note: Losses includes fails\n\n")
print("Wins: " + str(wins))
print("Losses: " + str(losses))
print("Fails: " + str(fails))
print("Success Rate: " + str(100 * wins/numRuns) + "%")



    # board = WordleBoard()
    # for i in range(0,5):
    #     board.takeGuess(input("Please enter a guess:\n"))
    #     board.verifyGuess()
    #     os.system('cls')
    #     board.printBoard()
    #     board.showWordBank()

    # print(board.word)