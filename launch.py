#-----------------------
# Andrew Johnson
# 20 May, 2016

# Text Based Python Game
#-----------------------

def prettyIntro(widthScr,gameDesc):
    """
    Launch screen visuals for text-based python game
    """
    print('+'*widthScr+"\n")
    line1 = "=======  |===\\   |===\\   |==="
    line2 = "    |     |    |  |    |  |    "
    line3 = "    |     |===<   |===/   |===\\"
    line4 = "    |     |    |  |       |   |"
    line5 = "    |     |===/   |       |===/"
    line6 = "\n"
    line7 = "Text-Based Python Game"
    lineList = [line1,line2,line3,line4,line5,line6,line7]
    for line in lineList:
        print("{str:^{spc}}".format(str = line,spc = widthScr))
    print("\n"+'+'*widthScr)
#    print(gameDesc)
    wrapDesc(widthScr,gameDesc)

def wrapDesc(w,str):
    """Print the game desciption with some padding on each side"""
    pad = 2     # leave pad/2 spaces on each side of the string
    cleanStr = str.replace('\n',' ')
    lenStr = len(str)
    fullLine = lenStr//(w-pad)
    lineLen = w-pad         # length of printable line
    for n in range(0,fullLine):
        print("{thisStr:^{width}}"\
            .format(thisStr = cleanStr[lineLen*n:lineLen*(n+1)],width = w))
    print("{thisStr:^{width}}".format(thisStr =cleanStr[lineLen*(n+1):],width = w ))
