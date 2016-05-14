def placeHolder(rowOne, rowTwo, rowThree, rowFour, rowFive, rowSix, rowSeven, rowEight, rowNine, rowTen):
    for i in range(0,10):
        rowOne.append('-')
        rowTwo.append('-')
        rowThree.append('-')
        rowFour.append('-')
        rowFive.append('-')
        rowSix.append('-')
        rowSeven.append('-')
        rowEight.append('-')
        rowNine.append('-')
        rowTen.append('-')




def buildGrid(rowOne, rowTwo, rowThree, rowFour, rowFive, rowSix, rowSeven, rowEight, rowNine, rowTen):
    print("\n")
    print(rowOne,"\n")
    print(rowTwo,"\n")
    print(rowThree,"\n")
    print(rowFour,"\n")
    print(rowFive,"\n")
    print(rowSix,"\n")
    print(rowSeven,"\n")
    print(rowEight,"\n")
    print(rowNine,"\n")
    print(rowTen)

def runGame():
    print('\n')
    rowOne = []
    rowTwo = []
    rowThree = []
    rowFour = []
    rowFive = []
    rowSix = []
    rowSeven = []
    rowEight = []
    rowNine = []
    rowTen = []
    placeHolder(rowOne, rowTwo, rowThree, rowFour, rowFive, rowSix, rowSeven, rowEight, rowNine, rowTen)
    buildGrid(rowOne, rowTwo, rowThree, rowFour, rowFive, rowSix, rowSeven, rowEight, rowNine, rowTen)

def main():
    runGame()


main()
