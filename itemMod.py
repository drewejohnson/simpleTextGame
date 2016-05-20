#--------------
# Andrew Johnson
# 20 May, 2016
#
# Simple Text-Based Game
#-------------

"""
This module contains classes for item creation plus a bunch of spawn-able items
"""

class RoomItem:
    itemName = ""
    itemType = ""
    equipSlot = ""
    desc = ""
# what type of item is it, where does it go, and a brief description
    def __init__(self,name):
        self.itemName = name

class Sword(RoomItem):
    def __init__(self,name):
        self.itemType = "sword"
        self.equipSlot = "hand"
        super().__init__(name)

#------------------------------
# Functions for room populating
#------------------------------
