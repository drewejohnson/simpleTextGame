#-----------------------
# Andrew Johnson
# Text Based Python Game
#-----------------------
"""module containing items and adjectives for spawning items"""
#---------------
# Imports
#---------------
import itemMod as IM
import roomMod as RM
#----------
# Functions
#----------

def populateItemAdj():
    """Submethod for populating lists of adjectives based on flags"""
    # Maybe iterate through IM.RoomItems.objects???
    # IM.Sword.lowRare = IM.adjPopulate(IM.lowRareAdj,'a')
    # IM.Sword.medRare = IM.adjPopulate(IM.medRareAdj,'a')
    # IM.Sword.highRare = IM.adjPopulate(IM.highRareAdj,'a')
    # IM.Axe.lowRare = IM.adjPopulate(IM.lowRareAdj,'a')
    # IM.Axe.medRare = IM.adjPopulate(IM.medRareAdj,'a')
    # IM.Axe.highRare = IM.adjPopulate(IM.highRareAdj,'a')
    # IM.Shield.lowRare = IM.adjPopulate(IM.lowRareAdj,'d')
    # IM.Shield.medRare = IM.adjPopulate(IM.medRareAdj,'d')
    # IM.Shield.highRare = IM.adjPopulate(IM.highRareAdj,'d')
    # IM.Helmet.lowRare = IM.adjPopulate(IM.lowRareAdj,'h')
    # IM.Helmet.medRare = IM.adjPopulate(IM.medRareAdj,'h')
    # IM.Helmet.highRare = IM.adjPopulate(IM.highRareAdj,'h')
    for r in range(1,4):
        IM.Sword.rAdj[r] = IM.adjPopulate(IM.allAdj[r],'a')
        IM.Axe.rAdj[r] = IM.adjPopulate(IM.allAdj[r],'a')
        IM.Shield.rAdj[r] = IM.adjPopulate(IM.allAdj[r],'d')
        IM.Helmet.rAdj[r] = IM.adjPopulate(IM.allAdj[r],'h')


# def inClass(itemAdj,itemClass):
#     """If itemAdj in a rarity dictionary of itemClass, return that dictionary"""
#     if itemAdj in itemClass.lowRare:
#         return itemClass.lowRare
#     elif itemAdj in itemClass.medRare:
#         return itemClass.medRare
#     elif itemAdj in itemClass.highRare:
#         return itemClass.highRare
#     else:
#         return 1
#
#
# def createAddItem(itemAdj,itemClass,sweep):
#     """
#     Creates an item of class itemClass and adds item to dictionary
#     of that class, if one does not exist already. Returns an object
#     instantiated with these characteristics.
#     """
#     whichRare = inClass(itemAdj,itemClass)
#     if whichRare != 1:
#         # adjective is a valid adjective
#         if not itemAdj in itemClass.objects:
#             # item with this name not created
#             itemClass.objects[itemAdj] = whichRare[itemAdj]
#             # add the item to the specific class of items (sword, axe,etc)
#             IM.RoomItem.objects[itemAdj] = itemClass(itemAdj,sweep)
#             # add the item to the overall item dictionary
#             RM.addToRoom(itemAdj,sweep)
#             del whichRare[itemAdj]
#             print('Added item {0} to class {1}'.\
#                 format(itemAdj,itemClass))
#             return IM.RoomItem.objects[itemAdj]
#             # return an instance of the item
#         else:
#             print('Item already exists in {}'.format(itemClass))
#             return 1
#     else:
#         print('Item {} not in adjective dictionaries'.format(itemAdj))
#         return 1


#--------------
# Build the Items
#--------------
# populateItemAdj()
# startSword = createAddItem("trusty",IM.Sword,RM.startSwp)
# startShield = createAddItem("reliable",IM.Shield,RM.startSwp)
