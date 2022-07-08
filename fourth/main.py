f = open("data.txt", "r") 
lines = f.readlines()

randomNumbers = "46,12,57,37,14,78,31,71,87,52,64,97,10,35,54,36,27,84,80,94,99,22,0,11,30,44,86,59,66,7,90,21,51,53,92,8,76,41,39,77,42,88,29,24,60,17,68,13,79,67,50,82,25,61,20,16,6,3,81,19,85,9,28,56,75,96,2,26,1,62,33,63,32,73,18,48,43,65,98,5,91,69,47,4,38,23,49,34,55,83,93,45,72,95,40,15,58,74,70,89".split(",")

""" TEST
randomNumbers = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1".split(",")

lines = [
    "22 13 17 11  0",
    " 8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    " 2  0 12  3  7",
    ""
]
"""

bingoBoards = []
flagBoards = []
boardAux = []
flagBoardAux = []
for idx, line in enumerate(lines):
    if line.strip() == "" or idx == (len(lines) - 1):
        flagBoards.append(flagBoardAux)
        bingoBoards.append(boardAux)
        flagBoardAux = []
        boardAux = []
        continue
    numbers = [int(x) for x in line.split() if x]
    boardAux.append(numbers)
    flagBoardAux.append([0,0,0,0,0])
#print("bingoBoards", bingoBoards)
#print("flagBoards", flagBoards)


win = False
lastWinNumber = 0
indexOfWinBoard = 0
for idxA, number in enumerate(randomNumbers):
    for idxB, board in enumerate(bingoBoards):
        for idxC, lineOfBoard in enumerate(board):
            for idxD, rowOfLineOfBoard in enumerate(lineOfBoard):
                if int(rowOfLineOfBoard) == int(number):
                    flagBoards[idxB][idxC][idxD] = 1
        
    for idxB, flagBoard in enumerate(flagBoards):
        for idxC, lineOfFlagBoard in enumerate(flagBoard):
            for idxD, rowOfLineOfBoard in enumerate(lineOfBoard):
                row = []
                for idxE, columnOfRow in enumerate(range(5)):
                    print("idxE", idxE, "idxD", idxD, "flagBoard index", idxB, "number", number)
                    print("numberBoard",bingoBoards[idxB][idxE][idxD])
                    row.append(flagBoard[idxE][idxD])
                win = all(flag == 1 for flag in row)
                if win:
                    print("WIN:", number)
                    print("TABLE INDEX:", idxB)
                    break
            if win:
                break
            win = all(flag == 1 for flag in lineOfFlagBoard)
            if win:
                print("WIN:", number)
                print("TABLE INDEX:", idxB)
                break
        if win:
            indexOfWinBoard = idxB
            break
    if win:
        lastWinNumber = number
        break
    
sumTotal = 0
for idxA, lineOfFlagBoard in enumerate(flagBoards[indexOfWinBoard]):
    for idxB, rowOfLineOfFlagBoard in enumerate(lineOfFlagBoard):
        if rowOfLineOfFlagBoard == 0:
            sumTotal += bingoBoards[indexOfWinBoard][idxA][idxB]
print("sumTotal:", sumTotal)
print("result:", sumTotal * int(lastWinNumber))