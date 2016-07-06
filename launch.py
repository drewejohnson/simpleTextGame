#-----------------------
# Andrew Johnson

# Text Based Python Game
#-----------------------
gameSpace = 60
def prettyIntro():
    """Launch screen visuals for text-based python game"""
    print('+'*gameSpace+"\n")
    line1 = "=======  |===\\   |===\\   |==="
    line2 = "    |     |    |  |    |  |    "
    line3 = "    |     |===<   |===/   |===\\"
    line4 = "    |     |    |  |       |   |"
    line5 = "    |     |===/   |       |===/"
    line6 = "\n"
    line7 = "Text-Based Python Game"
    lineList = [line1,line2,line3,line4,line5,line6,line7]
    for line in lineList:
        print("{str:^{spc}}".format(str = line,spc = gameSpace))
    print("\n"+'+'*gameSpace)

def prettyPrint(str):
    """Print a string, centered, with some padding on each side"""
    w = gameSpace
    pad = 2     # leave pad/2 spaces on each side of the string
#    cleanStr = str.replace('\n',' ')
    lenStr = len(str)
    fullLine = lenStr//(w-pad)
    lineLen = w-pad         # length of printable line
    for n in range(0,fullLine):
        print("{thisStr:^{width}}"\
            .format(thisStr = str[lineLen*n:lineLen*(n+1)],width = w))
    print("{thisStr:^{width}}".format(thisStr =str[lineLen*(n+1):],width = w ))


def launchScreen():
    """Driver for the launch screen of the game. Prints rules and objectives"""
    prettyIntro()
    prettyPrint(gameDesc.replace('\n',' '))
    prettyPrint(gameObjective.replace('\t',' '))
#    print(VFM.sortedVerbs)
    print("{s:^{w}}".format(s = "Commands: ",w = gameSpace))


def gameOver(enemyCls):
    """Player is dead. Clear all game space. Give player the option to restart"""
    from verbFuncMod import pName
    prettyPrint(deadHero.format(enemyCls.name.capitalize(),\
        enemyCls.className.capitalize(),pName.capitalize()))
    print("-"*gameSpace)
    print("-"*gameSpace)
    print("Do you wish to begin refreshed and renewed?")
    rStart = str(input("Press y to restart\n: ")).lower()
    if rStart == 'y':
        print("-"*gameSpace)
        print("\n\n\n")
        print("-"*gameSpace)
        from roomMod import buildGame, clearGame
        clearGame()
        return buildGame()
    else:
        raise SystemExit("Until next time, brave adventurer")

#--------
# Game descriptions
#-----------
gameDesc = "A simple text-based game where you explore a maze,fight monsters, and obtain gear."
gameObjective = "Traverse through the dangerous dungeon to defeat the boss "+\
    "located at the center. Defeat enemies as you encounter them, for they "+\
    "may be guarding valuable treasure. Enemies will become more difficult " +\
    "as you approach the center, but loot becomes more powerful as well. " +\
    "In combat, enemies will only attack you if you attack them first."
deadHero = "{0} the {1} hit back and killed our brave adventurer, {2}. \nSadness spreads over the land..."
