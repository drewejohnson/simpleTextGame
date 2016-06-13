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
        gobbly = CM.Goblin("gobbly",swp)
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
        nameInt = R.randint(0,len(CM.dragonNames))
        boss = CM.Dragon(CM.dragonNames[nameInt],swp)
        return 0
    else:
        for roll in range(roomRolls[diff]):
            rn1 = R.random()     # rarity
            rn2 = R.random()     # enemy or item
            rn3 = R.random()     # adjective for item/enemy
            if rn1 < rareThresh[diff][0]:
                diffRare = 1
            elif rn1 < rareThresh[diff][1]:
                diffRare = 2
            elif rn1 < rareThresh[diff][2]:
                diffRare = 3
            else:
                diffRare = 0        # no item/enemy spawned
            if diffRare > 0:
                if rn2 > splitIE[diff]:  # add an enemy to the room
    #----------------ENEMY SPAWN GOES HERE-------------------
                    return 0
                else:       # add an item to the room
                    itemChoice = {}
                    if len(IM.swordAdj[diff])>0:
                        itemChoice[IM.Sword] = IM.swordAdj[diff]
                    if len(IM.axeAdj[diff]) > 0:
                        itemChoice[IM.Axe]= IM.axeAdj[diff]
                    if len(IM.shieldAdj[diff]) > 0:
                        itemChoice[IM.Shield] = IM.shieldAdj[diff]
                    if len(IM.helmetAdj[diff]) > 0:
                        itemChoice[IM.Helmet] = IM.helmetAdj[diff]
                    thisType = R.choice(list(itemChoice.keys()))
                    thisAdj = R.choice(list(itemChoice[thisType].keys()))
                    thisItem = thisType(thisAdj,swp)
                    del itemChoice[thisType][thisAdj]
                    return 0
            else:
                print("Nothing added to room {}".format(sweepFunc(swp)))
                return 0 # nothing added to this room




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
#sweep = {}
# for y in range(1,roomsY+1):
#     for x in range(1,roomsX+1):
#         rooms[sweepFunc(x,y)] = RoomClass(sweepFunc(x,y))
        # print(x,y,roomDiff[y][x])
for s in range(1,roomsX*roomsY+1):
    rooms[s] = RoomClass(s)
    bflag = buildRoom(s,thisDiff(s))
    if bflag != 0:
        print('Error in building room {}.'.format(s))
        dummy = input('**')
