#-----------------------
# Andrew Johnson
# Text Based Python Game
#-----------------------
"""module containing items and adjectives for spawning items"""
#---------------
# Imports
#---------------
import itemMod as IM

#----------
# Functions
#----------

def buildItems():
    """Driver method for creating all weapons in the game"""
    populateItemAdj()
    # Generate starting items
    # createItem(IM.Sword,"trusty")
    # createItem(IM.Shield,'reliable')
    return None


def populateItemAdj():
    """Submethod for populating lists of adjectives based on flags"""
    # Maybe iterate through IM.RoomItems.objects???
    IM.Sword.lowRare = IM.adjPopulate(IM.lowRareAdj,'a')
    IM.Sword.medRare = IM.adjPopulate(IM.medRareAdj,'a')
    IM.Sword.highRare = IM.adjPopulate(IM.highRareAdj,'a')
    IM.Axe.lowRare = IM.adjPopulate(IM.lowRareAdj,'a')
    IM.Axe.medRare = IM.adjPopulate(IM.medRareAdj,'a')
    IM.Axe.highRare = IM.adjPopulate(IM.highRareAdj,'a')
    IM.Shield.lowRare = IM.adjPopulate(IM.lowRareAdj,'d')
    IM.Shield.medRare = IM.adjPopulate(IM.medRareAdj,'d')
    IM.Shield.highRare = IM.adjPopulate(IM.highRareAdj,'d')
    IM.Helmet.lowRare = IM.adjPopulate(IM.lowRareAdj,'h')
    IM.Helmet.medRare = IM.adjPopulate(IM.medRareAdj,'h')
    IM.Helmet.highRare = IM.adjPopulate(IM.highRareAdj,'h')


def inClass(itemClass,itemAdj):
    """If itemAdj in a rarity dictionary of itemClass, return that dictionary"""
    if itemAdj in itemClass.lowRare:
        return itemClass.lowRare
    elif itemAdj in itemClass.medRare:
        return itemClass.medRare
    elif itemAdj in itemClass.highRare:
        return itemClass.highRare
    else:
        return None


def createItem(itemClass,itemAdj):
    """Creates and returns an object in class itemClass with the adjective itemAdj"""
    inRareDict = inClass(itemClass,itemAdj)
    if inRareDict != None:
        newItemName = itemClass(itemAdj)
        # create new item in itemClass
        del inRareDict[itemAdj]     # remove adjective from dictionary
        return newItemName
    else:
        return None


startSword = IM.Sword("trusty",10)
startShield = IM.Shield("reliable",10)
