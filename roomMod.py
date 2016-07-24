#--------------
# Andrew Johnson
# 20 May, 2016
#
# Simple Text-Based Game
#-------------

"""
Functions for populating rooms with monsters
and gear, and will include the generation of the map
"""
#--------
# Imports
#--------
import classMod as CM
import itemMod as IM
# import Items
import random as R
import launch
import verbFuncMod as VFM
#--------
# classes
#--------
class RoomClass:
    """Class for a given room with items and enemies for that room"""

    def __init__(self,sweep):
        self.location = sweep
        self.items = {}
        self.enemies = {}

#------------------------------
# Functions for room populating
#------------------------------
def buildGame():
    IM.buildAdj()
    for s in range(1,roomsX*roomsY+1):
        rooms[s] = RoomClass(s)
        buildRoom(s,thisDiff(s))

def clearGame():
    for s in range(1,roomsX*roomsY+1):
        del rooms[s]


def sweepFunc(inX,inY = None):
    """Returns sweep value for two arguments, or tuple of coordinates for one"""
    if inY != None:
        return inX + (inY-1)*roomsX
    else:
        outY = inX // roomsX
        if inX % roomsX != 0:       # sweep value not perfectly divisible by roomsX
            outX = inX % roomsX
            outY += 1
        else:
            outX = roomsX
        return (outX,outY)


def thisDiff(s):
    """Returns the difficulty of a room given it's sweep value"""
    thisXY = sweepFunc(s)
    return roomDiff[thisXY[1]-1][thisXY[0]-1]


def buildRoom(swp,diff):
    """Add enemies and items to the room swp according to difficulty diff"""
    if diff == 0:       # player start room
        VFM.pName = input("\nWhat is your name, brave adventurer: \n")
        VFM.player = CM.Player(VFM.pName,swp)
        IM.startSword = IM.Sword("trusty",swp)
        IM.startShield = IM.Shield("reliable",swp)
        VFM.take(IM.startSword.itemName,IM.startSword.itemType)
        VFM.take(IM.startShield.itemName,IM.startShield.itemType)
        startPotion = IM.Potion(0,swp)
        print(VFM.take("potion"))
        gobbly = CM.Goblin("gobbly",swp,"unlucky")
        gobbly.values = [5,1,2]
        del IM.swordAdj[1]["trusty"]
        del IM.shieldAdj[1]['reliable']
        print(VFM.equip(IM.startSword.itemName,IM.startSword.itemType))
        print( VFM.equip(IM.startShield.itemName,IM.startShield.itemType))
        return 0
    elif diff == 4:     # boss room
        boss = CM.Dragon(R.choice(CM.dragonNames),swp)
        return 0
    else:
        for roll in range(0,roomRolls[diff]):
            rn1 = R.random()     # rarity
            rn2 = R.random()     # enemy or item
            if rn1 < rareThresh[diff][0]:
                diffRare = 1
            elif rn1 < rareThresh[diff][1]:
                diffRare = 2
            elif rn1 < rareThresh[diff][2]:
                diffRare = 3
            else:
                diffRare = diff-1
            if diffRare > 0:
                if rn2 > splitIE[diffRare]:  # add an enemy to the room
                    enemyChoice = {}
                    if len(CM.gobNames) > 0:
                        enemyChoice[CM.Goblin] = CM.gobNames
                    if len(CM.elfNames) > 0:
                        enemyChoice[CM.Elf] = CM.elfNames
                    if diff > 1 and len(CM.wizNames) > 0:
                        enemyChoice[CM.Wizard] = CM.wizNames
                    if len(CM.wolfNames) > 0:
                        enemyChoice[CM.Werewolf] = CM.wolfNames
                    if len(enemyChoice) == 0:
                        # print("No enemy names left {}".format(sweepFunc(swp)))
                        return 1
                    else:
                        thisType = R.choice(list(enemyChoice.keys()))
                        thisName = R.choice(list(enemyChoice[thisType]))
                        if diff > 1:
                            thisAdj = R.choice(list(IM.allAdj[diffRare]))
                            eStr = IM.allAdj[diffRare][thisAdj]
                        else:
                            thisAdj = None
                            eStr = None
                        thisEnemy = thisType(thisName,swp,thisAdj)
                        thisEnemy.enhance(eStr)
                else:       # add an item to the room
                    itemChoice = {}
                    if len(IM.swordAdj[diffRare])>0:
                        itemChoice[IM.Sword] = IM.swordAdj[diffRare]
                    if len(IM.axeAdj[diffRare]) > 0:
                        itemChoice[IM.Axe]= IM.axeAdj[diffRare]
                    if len(IM.shieldAdj[diffRare]) > 0:
                        itemChoice[IM.Shield] = IM.shieldAdj[diffRare]
                    if len(IM.helmetAdj[diffRare]) > 0:
                        itemChoice[IM.Helmet] = IM.helmetAdj[diffRare]
                    if (len(itemChoice) > 0):
                        thisType = R.choice(list(itemChoice.keys()))
                        thisAdj = R.choice(list(itemChoice[thisType].keys()))
                        thisItem = thisType(thisAdj,swp)
                        del itemChoice[thisType][thisAdj]
        if len(rooms[swp].enemies)>len(rooms[swp].items):
            for p in range(0,R.randint(1,diff)):
                thisPotion = IM.Potion(diff-1,swp)
                # print(p)
        return 0




#--------------------------
# Initialize the game space
#--------------------------
#------------------ Game parameters ------------
roomsX = 5
roomsY = 5
rooms = {}
bossSwp = sweepFunc(roomsX,roomsY)
roomDiff =  [[0,1,1,1,1],\
            [1,1,2,2,2],\
            [1,2,2,2,3],\
            [1,1,2,3,3],\
            [1,2,3,3,4]]
# 0 -> start room, 1-> low,2-> med,3-> high rare enemies/items,
# 4 -> boss
roomRolls = {1:2,2:3,3:4}
rareThresh = {1: [0.65,0.75,0.75],2:[0.15,0.7,0.77],3:[0.01,0.1,0.7]}
# threshold for finding a item/enemy of a given rarity/difficulty
splitIE = {1:0.6,2:0.5,3:0.35} # threshold for item/enemy generation
