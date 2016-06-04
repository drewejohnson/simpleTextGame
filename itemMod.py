#--------------
# Andrew Johnson
# 20 May, 2016
#
# Simple Text-Based Game
#-------------
"""Classes for item creation plus a bunch of spawn-able items"""
import roomMod as RM

class RoomItem:
    itemName = ""
    itemType = ""
    equipSlot = ""
    enhance = ""
    objects = {}        # actual items created
    lowRare = {}        # adjectives to be used
    medRare = {}
    highRare = {}

    def __init__(self,name,sweep):
        self.itemName = name
        RoomItem.objects[self.itemName] = self
        RM.addToRoom(name,sweep)


class Sword(RoomItem):
    objects = {}
    def __init__(self,name,sweep):
        self.itemType = "sword"
        self.equipSlot = "arms"
        super().__init__(name,sweep)

class Axe(RoomItem):
    objects = {}
    def __init__(self,name,sweep):
        self.itemType = "axe"
        self.equipSlot = "arms"
        super().__init__(name,sweep)

class Shield(RoomItem):
    objects = {}
    def __init__(self,name,sweep):
        self.itemType = "shield"
        self.equipSlot = "arms"
        super().__init__(name,sweep)

class Helmet(RoomItem):
    objects = {}
    def __init__(self,name):
        self.itemType = 'helmet'
        self.equipSlot = 'head'
        super().__init__(name,sweep)


#----------
# Functions
#----------
def adjPopulate(adjDict,adjFlag):
    """Method for populating the dictionary of adjectives for a specific item"""
# adjectives with enhancements starting with 'a' will go into dictionaries for weapons
# similarly, adjective enhancements leading with 'd' go to shields and 'h' for helmets
# Returns a dictionary corresponding to the key/values that match the flag
    passDict = {}

    for key in adjDict:
        if adjDict[key][0 ] == adjFlag:
            passDict[key] = adjDict[key]

    return passDict

#-----------
# Adjectives
#-----------
lowRareAdj = {
    "trusty":"a1",
    "reliable":"d1",
    "pointy":"a2",
    "durable":"d2",
    "shiny":"d2",
    "crooked":"a1",
    "decent":"a3",
    "adequate":"h1",
    "lucky":"d2a2h2",
    "smart":"h2",
    "unlucky": "a0"
}

medRareAdj = {
    "sharp":"a4",
    "sturdy":'d3',
    "protective":"d4a3h2",
    "viscious":"a4d4",
    "perceptive":"h4d2",
    "strong":"d5",
    "dangerous":"a5",
    "intimidating":"h5"
}

highRareAdj = {
    "legendary":"a7d5h5",
    "wise":"h7d5",
    "robust":"d7a5",
    "deadly":"a6d5"
}

allAdj = {}
for adj in lowRareAdj:
    allAdj[adj] = lowRareAdj[adj]
for adj in medRareAdj:
    allAdj[adj] = medRareAdj[adj]
for adj in highRareAdj:
    allAdj[adj] = highRareAdj[adj]
