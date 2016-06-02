#-------------------
# Andrew Johnson
#
# A Simple Text-Based Game
#---------------------
"""
A simple text-based game where you explore a maze,
fight monsters, and obtain gear.
"""

#----------------------
#	Modules Import
#----------------------

import verbFuncMod as VFM
import classMod as CM
import itemMod as IM
import roomMod as RM
import launch

#--------------
# Launch screen
#--------------
gameSpace = 40
launch.launchScreen(gameSpace,__doc__)

#------------
# Build rooms
#------------

#------------
# Creatures
#------------
gobbly = CM.Goblin("gobbly",10)
#RM.addToRoom('gobbly',10)

#------------
# Game
#------------

pName = input("What is your name, brave adventurer: \n")
player = CM.Player(pName.lower(),10)
#RM.addToRoom(pName,10)
startSword = IM.Sword("trusty",10)
#RM.addToRoom(startSword,10)
for x in range(1,26):
	print(x,RM.rooms[x].enemies,RM.rooms[x].items)

print(VFM.take(startSword.itemName))
print("And so, "+pName.capitalize()+" and their "+\
	startSword.itemName+' '+startSword.itemType+\
	" began their brave quest into the unknown!")
while True:
	VFM.getInput()
