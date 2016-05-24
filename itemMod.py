#--------------
# Andrew Johnson
# 20 May, 2016
#
# Simple Text-Based Game
#-------------

"""
This module contains classes for item creation plus
adjectives for enhancing objects
"""

class RoomItem:
    itemName = ""
    itemType = ""
    equipSlot = ""
    desc = ""
    objects = {}
# what type of item is it, where does it go, and a brief description
    def __init__(self,name):
        self.itemName = name
        RoomItem.objects[self.itemName] = self

class Sword(RoomItem):
    def __init__(self,name):
        self.itemType = "sword"
        self.equipSlot = "arms"
        super().__init__(name)

class Axe(RoomItem):
    def __init__(self,name):
        self.itemType = "axe"
        self.equipSlot = "arms"
        super().__init__(name)

class Shield(RoomItem):
    def __init__(self,name):
        self.itemType = "shield"
        self.equipSlot = "arms"
        super().__init__(name)

class Helmet(RoomItem):
    def __init__(self,name):
        self.itemType = 'helmet'
        self.equipSlot = 'head'
        super().__init__(name)

lowRareAdj = {
    "simple":"a1"
    "sturdy":"d1"
    "pointy":"a2"
    "durable":"d2"
    "shiny":"d2"
    "crooked":"a1"
    "decent":"a3"
    "adequate":"h1"
    "lucky":"d2a2h2"
    "smart":"h2"
}

medRareAdj = {
    "sharp":"a5"
    "protective":"d4a3h2"
    "viscious":"a5d4"
    "perceptive":"h4d3"
    "strong":"d5"
    "dangerous":"a6"
    "intimidating":"h"

}
highRareAdj = {
    "legendary":"a7d5h5"
    "wise":"h7d5"
    "robust":"d7a5"
    "deadly":"a6d5"
}
