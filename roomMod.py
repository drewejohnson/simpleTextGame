#--------------
# Andrew Johnson
# 20 May, 2016
#
# Simple Text-Based Game
#-------------

"""
This module contains functions for populating rooms with monsters
and gear, and will include the generation of the map
"""

roomsX = 5
roomsY = 5

rooms = {}
class RoomClass:
    """Class for a given room. Dictionaries are for items
        and enemies that are found in the room
    """
    items = {}
    enemies = {}
    location = []

    def __init__(self,sweep):
        self.location = sweep

#------------
# Basic Rooms
#------------

class startRoom(RoomClass):
    """First room. Mainly for testing features"""
    def __init__(self):
        self.location = [roomsX//2,1]
# Assume game space is a 5x5 grid. Start at center edge (5,0)
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



sweep = {}
for y in range(1,roomsY+1):
    for x in range(1,roomsX+1):
        sweep[sweepFunc(x,y)] = (x,y)
        rooms[sweepFunc(x,y)] = RoomClass(sweepFunc(sweepFunc(x,y)))
