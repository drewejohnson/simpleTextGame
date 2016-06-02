#--------------
# Andrew Johnson
# 20 May, 2016
#
# Simple Text-Based Game
#-------------

"""
This module contains classes for item creation plus
a bunch of spawn-able items
"""

import roomMod as RM

class RoomItem:
    itemName = ""
    itemType = ""
    equipSlot = ""
    desc = ""
    objects = {}
    location = []
# what type of item is it, where does it go, and a brief description
    def __init__(self,name,sweep):
        self.itemName = name
        RoomItem.objects[self.itemName] = self
        RM.addToRoom(name,sweep)

class Sword(RoomItem):
    def __init__(self,name,sweep):
        self.itemType = "sword"
        self.equipSlot = "arms"
        super().__init__(name,sweep)

class Axe(RoomItem):
    def __init__(self,name,sweep):
        self.itemType = "axe"
        self.equipSlot = "arms"
        super().__init__(name,sweep)

class Shield(RoomItem):
    def __init__(self,name,sweep):
        self.itemType = "shield"
        self.equipSlot = "arms"
        super().__init__(name,sweep)

class Helmet(RoomItem):
    def __init__(self,name):
        self.itemType = 'helmet'
        self.equipSlot = 'head'
        super().__init__(name,sweep)
