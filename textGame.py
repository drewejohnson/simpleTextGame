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
# Creatures
#------------
gobbly = CM.Goblin("gobbly",RM.roomsX//2+1,1)
#------------
# Game
#------------

pName = input("What is your name, brave adventurer: \n")
player = CM.Player(pName.lower(),RM.roomsX//2+1,1)
startSword = IM.Sword("trusty",RM.roomsX//2+1,1)
# Assume game space is a 5x5 grid. Start at center edge (5,0)
print(VFM.take(startSword.itemName))
print("And so, "+pName.capitalize()+" and their",\
	startSword.itemName,startSword.itemType,\
	"began their brave quest into the unknown!")
while True:
	VFM.getInput()
