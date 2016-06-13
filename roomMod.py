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


def addToRoom(item,sweep):
    """Adds an item or an enemy to the appropriate dictionary for room sweep"""
#----------can probably be deleted since items/enemies are added in buildRoom funciton
    if (item in IM.RoomItem.objects):
#        print('Adding '+str(item)+' to items')
        rooms[sweep].items[item] = IM.RoomItem.objects[item]
        return 0
    elif (item in CM.GameCharacter.objects):
#        print('Adding '+str(item)+' to characters')
        rooms[sweep].enemies[item] = CM.GameCharacter.objects[item]
        return 0
    else:
        return 1


def delFromRoom(item,sweep):
    """Removes an item from the room dictionary"""
#---------don't delete. Could still be useful for combat in removing enemies
    if (item in IM.RoomItem.objects):
        if item in rooms[sweep].items:
            del rooms[sweep].items[item]
            return 0
        else:
            print('No item in room {0} to remove'.format(sweep))
            return 2
    elif item in CM.GameCharacter.objects:
        if item in rooms[sweep].enemies:
            del rooms[sweep].enemies[item]
            return 0
        else:
            print('No item in room {0} to remove'.format(sweep))
            return 2
    else:
        print('Bad item {}'.format(item))
        return 1


def thisDiff(s):
    """Returns the difficulty of a room given it's sweep value"""
    thisXY = sweepFunc(s)
    return roomDiff[thisXY[1]-1][thisXY[0]-1]


def buildRoom(swp,diff):
    """Add enemies and items to the room swp according to difficulty diff"""
    if diff == 0:       # player start room
        gameSpace = 60
        launch.launchScreen(gameSpace)
        print(VFM.help())
        VFM.pName = input("\nWhat is your name, brave adventurer: \n")
        player = CM.Player('you',swp)
        gobbly = CM.Goblin("gobbly",swp,"unlucky")
        gobbly.values[1] = 0
        startSword = IM.Sword("trusty",swp)
        startShield = IM.Shield("reliable",swp)
        VFM.take(startSword.itemName)
        VFM.take(startShield.itemName)
        print(VFM.equip(startSword.itemName))
        print(VFM.equip(startShield.itemName))
        del IM.swordAdj[1]["trusty"]
        del IM.shieldAdj[1]['reliable']
        startStr = "Armed with their "+startSword.itemName+' '+\
        	startSword.itemType+' and '+startShield.itemName+' '+\
        	startShield.itemType+', '+VFM.pName.capitalize()+\
        	' departed into the darkness of the dungeon.'
        launch.prettyPrint(gameSpace,startStr)
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
            # print("Room: {0}, Roll: {1},DiffRare: {2}".\
            #     format(sweepFunc(swp),roll,diffRare))
            if diffRare > 0:
                if rn2 > splitIE[diffRare]:  # add an enemy to the room
                    enemyChoice = {}
                    if len(CM.gobNames) > 0:
                        enemyChoice[CM.Goblin] = CM.gobNames
                    if len(CM.elfNames) > 0:
                        enemyChoice[CM.Elf] = CM.elfNames
                    if len(CM.wizNames) > 0:
                        enemyChoice[CM.Wizard] = CM.wizNames
                    if len(CM.wolfNames) > 0:
                        enemyChoice[CM.Werewolf] = CM.wolfNames
                    if len(enemyChoice) == 0:
                        # print("No enemy names left {}".format(sweepFunc(swp)))
                        return 1
                    else:
                        thisType = R.choice(list(enemyChoice.keys()))
                        thisName = R.choice(list(enemyChoice[thisType]))
                        thisAdj = R.choice(list(IM.allAdj[diffRare]))
                        eStr = IM.allAdj[diffRare][thisAdj]
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
        return 0




#--------------------------
# Initialize the game space
#--------------------------
#------------------ Game parameters ------------
roomsX = 5
roomsY = 5
#startSwp = sweepFunc(1,1)
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

#------------------------------------------------
rooms = {}
for s in range(1,roomsX*roomsY+1):
    rooms[s] = RoomClass(s)
    bflag = buildRoom(s,thisDiff(s))
    if bflag != 0:
        print('Error in building room {}.'.format(sweepFunc(s)))
        dummy = input('**')
    # else:
    #     print("Room: {}".format(sweepFunc(s)))
    #     print(rooms[s].items)
    #     print(rooms[s].enemies)
