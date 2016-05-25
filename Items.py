#-----------------------
# Andrew Johnson
# Text Based Python Game
#-----------------------


"""module containing items and methods for spawning items"""

#---------------
# Module Import
#---------------
import itemMod as IM

#----------
# Functions
#----------

def buildItems():
    """Overarching method for creating all weapons in the game"""
    populateItemAdj()

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
#------------
# Starting items
#-------------
startSword = IM.Sword("trusty")
startShield = IM.Shield("reliable")
