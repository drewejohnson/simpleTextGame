#-----------------------
# Andrew Johnson
# 20 May, 2016

# Text Based Python Game
#-----------------------

import verbFuncMod as VFM
def prettyIntro(widthScr):
    """Launch screen visuals for text-based python game"""
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

def prettyPrint(w,str):
    """Print a string, centered, with some padding on each side"""
    pad = 2     # leave pad/2 spaces on each side of the string
#    cleanStr = str.replace('\n',' ')
    lenStr = len(str)
    fullLine = lenStr//(w-pad)
    lineLen = w-pad         # length of printable line
    for n in range(0,fullLine):
        print("{thisStr:^{width}}"\
            .format(thisStr = str[lineLen*n:lineLen*(n+1)],width = w))
    print("{thisStr:^{width}}".format(thisStr =str[lineLen*(n+1):],width = w ))


gameObjective = "Traverse through the dangerous dungeon to defeat the boss "+\
    "located at the center. Defeat enemies as you encounter them, for they "+\
    "may be guarding valuable treasure. Enemies will become more difficult " +\
    "as you approach the center, but loot becomes more powerful as well. " +\
    "In combat, enemies will only attack you if you attack them first."

def launchScreen(widthScr,gameDesc):
    """Driver for the launch screen of the game. Prints rules and objectives"""
    prettyIntro(widthScr)
    prettyPrint(widthScr,gameDesc.replace('\n',' '))
    prettyPrint(widthScr,gameObjective.replace('\t',' '))
#    print(VFM.sortedVerbs)
    print("{s:^{w}}".format(s = "Commands: ",w = widthScr))
    print(VFM.help())
