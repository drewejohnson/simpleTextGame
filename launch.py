#-----------------------
# Andrew Johnson
# 20 May, 2016

# Text Based Python Game
#-----------------------
"""
Launch screen visuals for text-based python game
"""

def prettyIntro(widthScr,gameDesc):
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
    print(gameDesc)
