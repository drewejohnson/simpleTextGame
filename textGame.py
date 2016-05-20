#-------------------
# Andrew Johnson
# 20 May, 2016
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

#------------
# Creatures
#------------
gobbly = CM.Goblin("Gobbly")
#------------
# Game
#------------
pName = input("What is your name, brave adventurer: \n")
player = CM.Adventurer(pName)
startSword = IM.Sword("trusty")
print(VFM.take(startSword.itemName))
print("And so, "+pName+" and their",startSword.itemName,startSword.itemType,\
	"began their brave quest into the unknown!")
while True:
	VFM.getInput()
