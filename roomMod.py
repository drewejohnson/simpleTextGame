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
#--------
# classes
#--------
class RoomClass:
    """Class for a given room with items and enemies for that room"""

    def __init__(self,sweep):
        self.location = sweep
        self.items = {}
        self.enemies = {}


class Room(RoomClass):
    """Generic room. Thought it would be helpful. Can be safely removed"""

    def __init__(self,sweep):
        super().__init__(sweep)
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
    """Removes and item from the room dictionary"""
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


#--------------------------
# Initialize the game space
#--------------------------
roomsX = 5
roomsY = 5
rooms = {}
#sweep = {}
for y in range(1,roomsY+1):
    for x in range(1,roomsX+1):
        rooms[sweepFunc(x,y)] = RoomClass(sweepFunc(x,y))
